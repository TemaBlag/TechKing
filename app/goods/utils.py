from re import search
from django.db.models import Value
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)
from django.db.models import Q


from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description", config="russian")
    query = SearchQuery(query, config="russian")

    result = (
        Products.objects.annotate(
            rank=SearchRank(
                vector,
                query,
                normalization=Value(2).bitor(Value(4)),
            )
        )
        .filter(rank__gt=0)
        .order_by("-rank")
    )
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )

    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )

    return result
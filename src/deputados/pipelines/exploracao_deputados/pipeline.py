"""
This is a boilerplate pipeline 'exploracao_deputados'
generated using Kedro 0.19.11
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from . import nodes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.baixar_deputados,
            inputs=[],
            outputs='deputados'
        ),
        node(
            nodes.sumarizar_por_partido,
            inputs=['deputados'],
            outputs='sumarizado'

        )
    ])

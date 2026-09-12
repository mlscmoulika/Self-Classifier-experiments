from kedro.pipeline import Node, Pipeline

from .nodes import (
 identify_fxn,   
)


def create_pipeline_model(**kwargs) -> Pipeline:
    """This is a simple pipeline which generates a pair of plots"""
    return Pipeline(
        [
            Node(
                func=identify_fxn,
                inputs="raw_cifar10_train",
                outputs="processed_cifar10_train",
                name="node_identify_fxn",
            ),
        ]
    )

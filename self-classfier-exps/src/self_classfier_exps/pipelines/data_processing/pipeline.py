from kedro.pipeline import Node, Pipeline

from .nodes import (
    cifar10_dataset,
    identity_fxn 
)


def create_pipeline_data_processing(**kwargs) -> Pipeline:
    return Pipeline(
        [
            
            Node(
                func=cifar10_dataset,
                inputs=["params:cifar10_dataset_root"],
                outputs=["raw_cifar10_train", "raw_cifar10_test"],
                name="node_raw_cifar10_train_test",
            ),
        ]
    )

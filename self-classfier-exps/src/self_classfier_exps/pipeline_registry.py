"""Project pipelines."""

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from .pipelines.experiments.pipeline import create_pipeline_experiments
from .pipelines.data_processing.pipeline import create_pipeline_data_processing
from .pipelines.model.pipeline import create_pipeline_model

def register_pipelines() -> dict[str, Pipeline]:
    exp_pipeline = create_pipeline_experiments()
    data_processing_pipeline = create_pipeline_data_processing()
    model_pipeline = create_pipeline_model()

    # 3. Map them to strings for CLI execution
    return {
        "experiments": exp_pipeline,
        "data_processing": data_processing_pipeline,
        "model": model_pipeline,

        # Define what runs if you type 'kedro run' without any --pipeline flag
        "__default__": exp_pipeline + data_processing_pipeline + model_pipeline
    }
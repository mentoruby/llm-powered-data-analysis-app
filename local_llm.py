from ray import serve
from ray.serve.llm import LLMConfig, build_openai_app


llm_config = LLMConfig(
    model_loading_config={
        'model_id': 'google/gemma-4-12B' # This can be ran in 16GB GPU
    },
    engine_kwargs={
        'max_num_batched_tokens': 8192,
        'max_model_len': 8192,
        'max_num_seqs': 64,
        'tensor_parallel_size': 1,
        'trust_remote_code': True,
    },
    accelerator_type='L4',
    deployment_config={
        'autoscaling_config': {
            'target_ongoing_requests': 32
        },
        'max_ongoing_requests': 64,
    },
)

# Build and deploy the model with OpenAI api compatibility:
llm_app = build_openai_app({"llm_configs": [llm_config]})
serve.run(llm_app)
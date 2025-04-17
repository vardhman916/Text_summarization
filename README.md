End to end text summarization project 
##workflow
1:- update config yaml
# config.yaml

data_ingestion:
  root_dir: artifacts/data_ingestion
  source_url: https://your-dataset-url.com/data.zip
  local_data_file: artifacts/data_ingestion/data.zip
  unzip_dir: artifacts/data_ingestion/raw_data

data_validation:
  root_dir: artifacts/data_validation
  status_file: artifacts/data_validation/status.txt
  schema_file: config/schema.yaml

data_transformation:
  root_dir: artifacts/data_transformation
  tokenizer_name: t5-base
  transformed_data_dir: artifacts/data_transformation/tokenized_data

model_trainer:
  root_dir: artifacts/model_trainer
  model_ckpt: artifacts/model_trainer/checkpoints
  saved_model: artifacts/model_trainer/final_model

model_evaluation:
  root_dir: artifacts/model_evaluation
  report_file: artifacts/model_evaluation/report.json

prediction:
  root_dir: artifacts/prediction
  input_file: artifacts/prediction/input.txt
  output_file: artifacts/prediction/summary.txt

2. params.yaml
# params.yaml

model_params:
  model_name: t5-small
  max_input_length: 512
  max_target_length: 128
  batch_size: 8
  num_train_epochs: 3
  learning_rate: 3e-5
  weight_decay: 0.01
  warmup_steps: 500

training:
  use_gpu: true
  seed: 42
  logging_steps: 100

evaluation:
  metric: rouge
  eval_batch_size: 4


  Task	                           Use from
Folder & file paths	               config.yaml
Hyperparameters & training	       params.yaml

3. entity
4. configuration
5. update the configuration manager in src config
6. update the components
7. pipeline
8. main.py
9 update app.py
 config.yaml = all file path
 constants = read config.yaml and params.yaml
 common = read yaml, create direct,get size
 entity = here we will paste dataValidationConfig
 Config1 = get_data_validation_config









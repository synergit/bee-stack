# 🐝 Bee Stack

![Bee Stack Demo Video](https://media.githubusercontent.com/media/i-am-bee/bee-stack/refs/heads/assets/docs/assets/bee-stack-demo.gif)

The Bee Stack repository provides everything you need to run the Bee Application Stack locally using **Docker Compose**. This setup allows you to run, test, and experiment with Bee's various components seamlessly.

## 🧩 Bee Stack Components

The Bee Stack comprises the following components, each contributing distinct functionalities to support your AI-driven applications:

- [bee-agent-framework](https://github.com/i-am-bee/bee-agent-framework) gives the foundation to build LLM Agents.
- [bee-code-interpreter](https://github.com/i-am-bee/bee-code-interpreter) runs a user or generated Python code in a sandboxed environment.
- [bee-api](https://github.com/i-am-bee/bee-api) exposes agents via OpenAPI compatible Rest API.
- [bee-ui](https://github.com/i-am-bee/bee-ui) allows you to create agents within your web browser.
- [bee-observe](https://github.com/i-am-bee/bee-observe) and [bee-observe-connector](https://github.com/i-am-bee/bee-observe-connector) help you to trace what you are agents are doing.

![architecture](https://raw.githubusercontent.com/i-am-bee/bee-stack/refs/heads/assets/docs/assets/architecture.svg)

## 🔧 Pre-requisities
**[Docker](https://www.docker.com/)** or similar container engine including docker
compose ([Rancher desktop](https://docs.rancherdesktop.io/) or [Podman](https://podman.io/))
> ⚠️ IMPORTANT: Make sure your VM has at least 8GB of RAM configured

> ⚠️ Warning: A **rootless machine is not supported** (e.g. if you use podman,
> [set your VM to rootful](https://docs.podman.io/en/stable/markdown/podman-machine-set.1.html#examples))

## 🏃‍♀️ Usage

### Inital setup
```shell
git clone https://github.com/i-am-bee/bee-stack.git
cd bee-stack
# Run setup script to configure LLM provider and start the stack
./bee-stack.sh setup
```


### Commands
You can use the following commands
```shell
./bee-stack.sh start # start the stack (this can take a while)
./bee-stack.sh stop  # stop the stack without removing data
./bee-stack.sh clean # remove data
./bee-stack.sh setup # reconfigure (e.g. to switch LLM provider)
```
Once started you can find use the following URLs:

- bee-ui: http://localhost:3000
- mlflow: http://localhost:8080
- bee-api: http://localhost:4000 (for direct use of the api, use apiKey `sk-testkey`)
- list all open ports: `docker compose ps --format "{{.Names}}: {{.Ports}}"`

##  ⛓️‍💥 Troubleshooting
Please see our [troubleshoting guide](docs/troubleshooting.md) for help with the most common issues.

> If you run through the troubleshooting guide and bee-stack is still crashing, please collect
> the logs using `./bee-stack.sh logs` and submit them to a new issue at:
> https://github.com/i-am-bee/bee-agent-framework/issues/new?template=run_stack_issue.md

## 👷 Advanced

### Custom models
To create a bee with a custom model other than the default for the provider, you can use the API 
through [bee-python-sdk](https://github.com/i-am-bee/bee-python-sdk) or directly:

```shell
curl -X POST \
  "${BEE_API:-localhost:4000}/v1/assistants" \
  -H "Authorization: Bearer ${BEE_API_KEY:-sk-proj-testkey}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my bee with a custom model",
    "model": "meta-llama/llama-3-1-8b-instruct"
  }'
```
You can then find edit the bee in the UI (assign tools, role, etc.)

### Manual configuration

If the setup script is not working for you (e.g. you don't have bash installed), you can
configure `.env` manually, have a look at [example.env](example.env) file.

> ⚠️ Warning: If you change providers, the default bee will stop working, because it is configured with a model from the previous provider. You should create a new Bee or remove all data using `docker compose --profile all down --volumes`.

### Advanced docker compose commands
You can use any typical compose commands to inspect the state of the services:
```shell
# Docker
docker compose ps
docker compose logs bee-api

# Podman
podman compose ps
podman compose logs bee-api
```

### For developers
If you are a developer on `bee-api` or `bee-ui` and want to run only the supporting infrastructure,
use the profile `infra`, e.g.:

```shell
./bee-stack.sh start:infra
```

## Contribution guidelines

The Bee Agent Framework is an open-source project and we ❤️ contributions.

If you'd like to contribute to Bee, please take a look at our [contribution guidelines](./CONTRIBUTING.md).

## Contributors

Special thanks to our contributors for helping us improve Bee Agent Framework.

<a href="https://github.com/i-am-bee/bee-stack/graphs/contributors">
  <img alt="Contributors list" src="https://contrib.rocks/image?repo=i-am-bee/bee-stack" />
</a>


## Chloe's Notes
```bash
./bee-stack.sh start
>>>> Executing external compose provider "/usr/local/bin/docker-compose". Please see podman-compose(1) for how to disable this message. <<<<

bee-stack is not yet configured, do you want to configure it now? (Y/n): Y
🐝 Welcome to the bee-stack! You're just a few questions away from building agents!
(Press ^C to exit)

Choose LLM provider:
[1]: watsonx
[2]: ollama
[3]: bam
[4]: openai
Select [1-4]: 1
Provide WATSONX_PROJECT_ID:  ****
Provide WATSONX_API_KEY: ****
Provide WATSONX_REGION (leave empty for default 'us-south'): 
Do you want to start bee-stack now? (Y/n): Y
>>>> Executing external compose provider "/usr/local/bin/docker-compose". Please see podman-compose(1) for how to disable this message. <<<<

[+] Running 45/3
 ✔ bee-ui Pulled                                                           7.5s 
 ✔ bee-usercontent-site Pulled                                             8.7s 
 ✔ bee-api Pulled                                                         34.0s 
[+] Running 12/12
 ✔ Container bee-stack-bee-usercontent-site-1      Sta...                                             20.7s 
 ✔ Container bee-stack-collector-1                 Started                                            20.6s 
 ✔ Container bee-stack-bee-code-interpreter-k3s-1  Started                                            20.8s 
 ✔ Container bee-stack-milvus-1                    Started                                            21.1s 
 ✔ Container bee-stack-bee-api-1                   Healthy                                            35.5s 
 ✔ Container bee-stack-bee-observe-1               Started                                            21.0s 
 ✔ Container bee-stack-etcd-1                      Started                                            19.1s 
 ✔ Container bee-stack-mlflow-1                    Started                                            10.7s 
 ✔ Container bee-stack-mongo-1                     Healthy                                            14.7s 
 ✔ Container bee-stack-minio-1                     Started                                            10.7s 
 ✔ Container bee-stack-redis-1                     Started                                            10.6s 
 ✔ Container bee-stack-bee-ui-1                    Started                                            24.1s 
Done. You can visit the UI at http://localhost:3000
>>>> Executing external compose provider "/usr/local/bin/docker-compose". Please see podman-compose(1) for how to disable this message. <<<<

[+] Running 12/12
 ✔ Container bee-stack-bee-code-interpreter-k3s-1  Started                                            20.8s 
 ✔ Container bee-stack-collector-1                 Started                                            20.6s 
 ✔ Container bee-stack-bee-usercontent-site-1      Sta...                                             20.8s 
 ✔ Container bee-stack-milvus-1                    Started                                            21.2s 
 ✔ Container bee-stack-bee-api-1                   Healthy                                            37.1s 
 ✔ Container bee-stack-bee-observe-1               Started                                            21.0s 
 ✔ Container bee-stack-etcd-1                      Started                                            20.5s 
 ✔ Container bee-stack-mlflow-1                    Started                                            10.6s 
 ✔ Container bee-stack-minio-1                     Started                                            10.8s 
 ✔ Container bee-stack-mongo-1                     Healthy                                            15.3s 
 ✔ Container bee-stack-redis-1                     Started                                            10.5s 
 ✔ Container bee-stack-bee-ui-1                    Started                                            26.6s 
Done. You can visit the UI at http://localhost:3000
```

Note that a .env file is generated after the setup input, the setup command is 
```bash
LLM_BACKEND=watsonx
EMBEDDING_BACKEND=watsonx
WATSONX_PROJECT_ID=****
WATSONX_API_KEY=****
WATSONX_REGION=us-south
```

To run the streamlit application for paper summarization
```bash
streamlit run generated_source_code/paper-summary-no-llm-decorator.py
```

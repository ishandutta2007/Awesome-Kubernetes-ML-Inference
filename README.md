# Awesome-Kubernetes-ML-Inference

## Top Kubernetes ML Inference Ecosystem



**Curated List of SaaS Products & Open-Source GitHub Projects**  

*Focused on Model Serving, GPU Optimization & Production Inference at Scale*  

**Last updated: October 2026**



This repository tracks notable **SaaS platforms** and **open-source projects** for **Kubernetes ML Inference**. These tools deploy, scale, and serve machine learning models — from traditional predictive models to large language models — on Kubernetes with production-grade autoscaling, GPU optimization, and intelligent routing.



**Examples** include Google Vertex AI, AWS SageMaker, Azure Machine Learning, Databricks, Dataiku, DataRobot, H2O.ai, Domino Data Lab, Scale AI, and BentoML (the category leaders).



**Open-source emphasis**: This section is heavily expanded with every major active project for self-hosting, GPU-aware scheduling, and transparent inference infrastructure — ideal for ML engineers, platform teams, and organizations building vendor-neutral Kubernetes-native serving stacks.



Contributions welcome! Open a PR to add/update entries. Keep descriptions factual and link to official sites.



## Table of Contents

- [SaaS/Hosted Platforms](#saas-hosted-platforms)

- [Open-Source GitHub Projects](#open-source-github-projects)

- [How to Contribute](#how-to-contribute)

- [Disclaimer](#disclaimer)



## SaaS/Hosted Platforms



- **[Google Vertex AI](https://cloud.google.com/vertex-ai)**  

  Google's end-to-end ML platform with Model Garden for open models, prediction endpoints, and Vertex AI Agent Builder. Strong integration with GKE for hybrid serving.



- **[AWS SageMaker](https://aws.amazon.com/sagemaker/)**  

  Fully managed ML platform with real-time inference endpoints, serverless inference, and asynchronous batch transform. Supports Triton, vLLM, and custom containers on EKS.



- **[Azure Machine Learning](https://azure.microsoft.com/en-us/products/machine-learning/)**  

  Microsoft's managed ML platform with managed online endpoints, batch inference, and Azure OpenAI Service integration. Native AKS integration for Kubernetes serving.



- **[Databricks](https://www.databricks.com/)**  

  Unified analytics platform with Model Serving for ML models and LLMs, featuring auto-scaling, GPU optimization, and native MLflow integration.



- **[Dataiku](https://www.dataiku.com/)**  

  Enterprise AI platform with visual model development, deployment, and monitoring capabilities across cloud and on-prem environments.



- **[DataRobot](https://www.datarobot.com/)**  

  Automated machine learning platform with deployment, monitoring, and governance features for enterprise AI.



- **[H2O.ai](https://h2o.ai/)**  

  Open-source ML platform (with enterprise offerings) featuring Driverless AI for automated model building and deployment.



- **[Domino Data Lab](https://www.domino.ai/)**  

  Enterprise MLOps platform for model development, deployment, and monitoring with reproducibility focus.



- **[Scale AI](https://scale.com/)**  

  Data labeling and model evaluation platform with fine-tuning services and deployment support.



- **[BentoML](https://www.bentoml.com/)**  

  Model serving framework (with hosted BentoCloud) offering adaptive batching, multi-model composition, and scale-to-zero. Python-first with Runner abstraction for custom inference logic.



## Open-Source GitHub Projects



- **[KServe](https://github.com/kserve/kserve)**  

  **The standard Kubernetes-native model serving platform** — CNCF project with 5,000+ stars. Provides `InferenceService` CRD abstracting autoscaling, networking, health checking, and server configuration. Supports TensorFlow, PyTorch, XGBoost, scikit-learn, ONNX, and Hugging Face. Features **scale-to-zero**, **canary rollouts**, **GPU autoscaling**, and **multi-node inference** for large LLMs . v0.20 adds confidential model serving with TEE hardware attestation and KV cache offloading for vLLM .



- **[KubeRay / Ray Serve](https://github.com/ray-project/ray)**  

  **Distributed serving on Kubernetes** — Ray Serve builds on Ray to orchestrate multi-model pipelines, heterogeneous GPU workloads, and autoscaling inference services. Excellent for ensemble models combining gradient boosting and neural networks .



- **[NVIDIA Triton Inference Server](https://github.com/triton-inference-server/server)**  

  **High-performance multi-framework inference server** — supports TensorFlow, PyTorch, ONNX, TensorRT, and tree models via FIL backend. Dynamic batching and GPU optimization. Requires external K8s HPA/KEDA for autoscaling (no built-in elasticity) .



- **[Seldon Core v2](https://github.com/SeldonIO/seldon-core)**  

  **Kubernetes model deployment with pipeline DAGs** — v2.x is Apache 2.0 licensed (v1.x was BUSL-1.1, verify version before commercial use). Features drift detection, canary rollouts, and native Experiment/Canary objects for A/B testing .



- **[BentoML](https://github.com/bentoml/BentoML)**  

  **Python-first serving framework** — Runner abstraction for custom inference logic, adaptive batching, and multi-model pipelines. Faster cold starts than KServe for serverless deployments .



- **[vLLM](https://github.com/vllm-project/vllm)**  

  **Production-default LLM inference engine** — PagedAttention for memory-efficient KV cache management, continuous batching, and prefix caching. Red Hat is largest corporate contributor .



- **[SGLang](https://github.com/sgl-project/sglang)**  

  **Fastest inference engine for chat and agents** — RadixAttention for KV cache reuse across related requests. Native disaggregated inference support .



- **[NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo)**  

  **Production-grade disaggregated inference framework** — native prefill/decode separation with RDMA/NVLink KV cache transfer. Supports vLLM, SGLang, and TensorRT-LLM backends at data center scale .



- **[MLOX](https://github.com/MLOX/MLOX)**  

  **Open-source MLOps for small teams and research** — backend-agnostic orchestration supporting Docker, Kubernetes, Native, and Connector backends. Service-centric model: deploy MLflow, Airflow, OpenBao, and MLServer with simple CLI commands. Integrated secrets management and TLS termination. Best for development and testing phases, not large-scale production .



### Additional Strong Open-Source Options



- **[Kubeflow](https://github.com/kubeflow/kubeflow)** — ML toolkit for Kubernetes including Pipelines, Katib (hyperparameter tuning), and KFServing (KServe predecessor) .

- **[NVIDIA NIM](https://www.nvidia.com/en-us/ai/)** — Optimized inference microservices for foundation models; pairs with KServe for deployment orchestration .

- **[Hugging Face TGI](https://github.com/huggingface/text-generation-inference)** — LLM serving with token streaming, continuous batching, and quantization support.

- **[llm-d](https://github.com/llm-d/llm-d)** — Kubernetes-native distributed inference scheduler for disaggregated prefill/decode workloads; complements KServe for cluster-wide KV-cache-aware routing .

- **[LMCache](https://github.com/LMCache/LMCache)** — Distributed KV cache layer for LLM serving; integrates with KServe for reduced TTFT and improved multi-turn QA performance .



**Frameworks for building custom systems**: Combine **KServe** for model lifecycle orchestration, **vLLM** or **SGLang** for inference execution, **llm-d** for cluster-wide routing, and **KEDA** for LLM-specific autoscaling. For multi-framework deployments, layer **Triton** with **KServe** for ensemble models. For lightweight MLOps on Kubernetes, **MLOX** provides integrated secrets and service orchestration .



**Key architectural insight**: The serving stack is layered — **KServe** handles deployment lifecycle and governance, **vLLM/SGLang** handle efficient execution, **llm-d** adds cluster-wide cache-aware routing, and **Triton** serves multi-framework predictive models. For LLM workloads, KServe's `LLMInferenceService` provides OpenAI-compatible endpoints (`/v1/chat/completions`, `/v1/responses`) with KV cache offloading and multi-node tensor parallelism .



## How to Contribute



1. Fork the repo.

2. Add/edit entries in `README.md` (follow existing format).

3. Include: name, link, 1–2 sentence description, and whether it's SaaS or open-source.

4. Submit PR with a short explanation.



Star the repo if you find it useful!



## Disclaimer



- This is a **community-curated** list — not exhaustive and not an endorsement.

- **License awareness is critical**: Seldon Core v1.x is BUSL-1.1 (restricts commercial hosting); v2.x is Apache 2.0. KServe, Triton, BentoML, Ray, vLLM, and SGLang are Apache 2.0 or BSD — safe for commercial use .

- Kubernetes ML inference requires GPU capacity planning, KV cache management, and proper autoscaling configuration for production workloads.

- Self-hosted solutions require Kubernetes operational expertise and regular security updates.



---



**Made for ML engineers, platform architects, AI infrastructure teams, and open-source enthusiasts.**  

Let's make Kubernetes ML inference more open, scalable, and vendor-neutral.
# Awesome-Kubernetes-ML-Inference


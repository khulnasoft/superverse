# MetaVision

[notebooks](https://github.com/khulnasoft/notebooks) | [inference](https://github.com/khulnasoft/inference) | [autodistill](https://github.com/autodistill/autodistill) | [maestro](https://github.com/khulnasoft/multimodal-maestro)

<br>

[![version](https://badge.fury.io/py/metavision.svg)](https://badge.fury.io/py/metavision)
[![downloads](https://img.shields.io/pypi/dm/metavision)](https://pypistats.org/packages/metavision)
[![snyk](https://snyk.io/advisor/python/metavision/badge.svg)](https://snyk.io/advisor/python/metavision)
[![license](https://img.shields.io/pypi/l/metavision)](https://github.com/khulnasoft/metavision/blob/main/LICENSE.md)
[![python-version](https://img.shields.io/pypi/pyversions/metavision)](https://badge.fury.io/py/metavision)
[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/khulnasoft/metavision/blob/main/demo.ipynb)
[![gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/Khulnasoft/Annotators)
[![discord](https://img.shields.io/discord/1159501506232451173?logo=discord&label=discord&labelColor=fff&color=5865f2&link=https%3A%2F%2Fdiscord.gg%2FGbfgXGJ8Bk)](https://discord.gg/GbfgXGJ8Bk)
[![built-with-material-for-mkdocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)

</div>

## 👋 hello

**We write your reusable computer vision tools.** Whether you need to load your dataset from your hard drive, draw detections on an image or video, or count how many detections are in a zone. You can count on us! 🤝

## 💻 install

Pip install the metavision package in a
[**Python>=3.8**](https://www.python.org/) environment.

```bash
pip install metavision
```

Read more about conda, mamba, and installing from source in our [guide](https://khulnasoft.github.io/metavision/).

## 🔥 quickstart

### models

Metavision was designed to be model agnostic. Just plug in any classification, detection, or segmentation model. For your convenience, we have created [connectors](https://metavision.khulnasoft.com/latest/detection/core/#detections) for the most popular libraries like Ultralytics, Transformers, or MMDetection.

```python
import cv2
import metavision as sv
from ultralytics import YOLO

image = cv2.imread(...)
model = YOLO("yolov8s.pt")
result = model(image)[0]
detections = sv.Detections.from_ultralytics(result)

len(detections)
# 5
```

<details>
<summary>👉 more model connectors</summary>

- inference

  ```python
  import cv2
  import metavision as sv
  from inference import get_model

  image = cv2.imread(...)
  model = get_model(model_id="yolov8s-640", api_key=<KHULNASOFT API KEY>)
  result = model.infer(image)[0]
  detections = sv.Detections.from_inference(result)

  len(detections)
  # 5
  ```

</details>

### annotators

```python
import cv2
import metavision as sv

image = cv2.imread(...)
detections = sv.Detections(...)

box_annotator = sv.BoxAnnotator()
annotated_frame = box_annotator.annotate(
  scene=image.copy(),
  detections=detections)
```

### datasets

```python
import metavision as sv
from khulnasoft import Khulnasoft

project = Khulnasoft().workspace(<WORKSPACE_ID>).project(<PROJECT_ID>)
dataset = project.version(<PROJECT_VERSION>).download("coco")

ds = sv.DetectionDataset.from_coco(
    images_directory_path=f"{dataset.location}/train",
    annotations_path=f"{dataset.location}/train/_annotations.coco.json",
)

path, image, annotation = ds[0]
    # loads image on demand

for path, image, annotation in ds:
    # loads image on demand
```

<details close>
<summary>👉 more dataset utils</summary>

- load

  ```python
  dataset = sv.DetectionDataset.from_yolo(
      images_directory_path=...,
      annotations_directory_path=...,
      data_yaml_path=...
  )

  dataset = sv.DetectionDataset.from_pascal_voc(
      images_directory_path=...,
      annotations_directory_path=...
  )

  dataset = sv.DetectionDataset.from_coco(
      images_directory_path=...,
      annotations_path=...
  )
  ```

- split

  ```python
  train_dataset, test_dataset = dataset.split(split_ratio=0.7)
  test_dataset, valid_dataset = test_dataset.split(split_ratio=0.5)

  len(train_dataset), len(test_dataset), len(valid_dataset)
  # (700, 150, 150)
  ```

- merge

  ```python
  ds_1 = sv.DetectionDataset(...)
  len(ds_1)
  # 100
  ds_1.classes
  # ['dog', 'person']

  ds_2 = sv.DetectionDataset(...)
  len(ds_2)
  # 200
  ds_2.classes
  # ['cat']

  ds_merged = sv.DetectionDataset.merge([ds_1, ds_2])
  len(ds_merged)
  # 300
  ds_merged.classes
  # ['cat', 'dog', 'person']
  ```

- save

  ```python
  dataset.as_yolo(
      images_directory_path=...,
      annotations_directory_path=...,
      data_yaml_path=...
  )

  dataset.as_pascal_voc(
      images_directory_path=...,
      annotations_directory_path=...
  )

  dataset.as_coco(
      images_directory_path=...,
      annotations_path=...
  )
  ```

- convert

  ```python
  sv.DetectionDataset.from_yolo(
      images_directory_path=...,
      annotations_directory_path=...,
      data_yaml_path=...
  ).as_pascal_voc(
      images_directory_path=...,
      annotations_directory_path=...
  )
  ```

</details>

<br/>

## 💜 built with metavision

Did you build something cool using metavision? [Let us know!](https://github.com/khulnasoft/metavision/discussions/categories/built-with-metavision)

https://user-images.githubusercontent.com/26109316/207858600-ee862b22-0353-440b-ad85-caa0c4777904.mp4

https://github.com/khulnasoft/metavision/assets/26109316/c9436828-9fbf-4c25-ae8c-60e9c81b3900

https://github.com/khulnasoft/metavision/assets/26109316/3ac6982f-4943-4108-9b7f-51787ef1a69f

## 📚 documentation

Visit our [documentation](https://khulnasoft.github.io/metavision) page to learn how metavision can help you build computer vision applications faster and more reliably.

## 🏆 contribution

We love your input! Please see our [contributing guide](https://github.com/khulnasoft/metavision/blob/main/CONTRIBUTING.md) to get started. Thank you 🙏 to all our contributors!

<p align="center">
    <a href="https://github.com/khulnasoft/metavision/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=khulnasoft/metavision" />
    </a>
</p>

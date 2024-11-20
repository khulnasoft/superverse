---
comments: true
status: new
---

# Annotators

=== "VertexAnnotator"

    ```python
    import metavision as sv

    image = ...
    key_points = sv.KeyPoints(...)

    vertex_annotator = sv.VertexAnnotator(
        color=sv.Color.GREEN,
        radius=10
    )
    annotated_frame = vertex_annotator.annotate(
        scene=image.copy(),
        key_points=key_points
    )
    ```

    <div class="result" markdown>

    ![vertex-annotator-example](https://media.khulnasoft.com/metavision-annotator-examples/vertex-annotator-example.png){ align=center width="800" }

    </div>

=== "EdgeAnnotator"

    ```python
    import metavision as sv

    image = ...
    key_points = sv.KeyPoints(...)

    edge_annotator = sv.EdgeAnnotator(
        color=sv.Color.GREEN,
        thickness=5
    )
    annotated_frame = edge_annotator.annotate(
        scene=image.copy(),
        key_points=key_points
    )
    ```

    <div class="result" markdown>

    ![edge-annotator-example](https://media.khulnasoft.com/metavision-annotator-examples/edge-annotator-example.png){ align=center width="800" }

    </div>

=== "VertexLabelAnnotator"

    ```python
    import metavision as sv

    image = ...
    key_points = sv.KeyPoints(...)

    vertex_label_annotator = sv.VertexLabelAnnotator(
        color=sv.Color.GREEN,
        text_color=sv.Color.BLACK,
        border_radius=5
    )
    annotated_frame = vertex_label_annotator.annotate(
        scene=image.copy(),
        key_points=key_points
    )
    ```

    <div class="result" markdown>

    ![vertex-label-annotator-example](https://media.khulnasoft.com/metavision-annotator-examples/vertex-label-annotator-example.png){ align=center width="800" }

    </div>

<div class="md-typeset">
  <h2><a href="#metavision.keypoint.annotators.VertexAnnotator">VertexAnnotator</a></h2>
</div>

:::metavision.keypoint.annotators.VertexAnnotator

<div class="md-typeset">
  <h2><a href="#metavision.keypoint.annotators.EdgeAnnotator">EdgeAnnotator</a></h2>
</div>

:::metavision.keypoint.annotators.EdgeAnnotator

<div class="md-typeset">
  <h2><a href="#metavision.keypoint.annotators.VertexLabelAnnotator">VertexLabelAnnotator</a></h2>
</div>

:::metavision.keypoint.annotators.VertexLabelAnnotator

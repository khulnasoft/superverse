---
comments: true
status: deprecated
---

# Deprecated

These features are phased out due to better alternatives or potential issues in future versions. Deprecated functionalities are supported for **five subsequent releases**, providing time for users to transition to updated methods.

- Constructing [`DetectionDataset`](https://superverse.khulnasoft.com/latest/datasets/core/#superverse.dataset.core.DetectionDataset) and [`ClassificationDataset`](https://superverse.khulnasoft.com/latest/datasets/core/#superverse.dataset.core.ClassificationDataset) with parameter `images` as `Dict[str, np.ndarray]` will be removed in `superverse-0.26.0`. Please pass a list of paths `List[str]` instead.

- The `DetectionDataset.images` property will be removed in `superverse-0.26.0`. Please loop over images with `for path, image, annotation in dataset:`, as that does not require loading all images into memory.

- `BoundingBoxAnnotator` has been renamed to `BoxAnnotator` after the old implementation of [`BoxAnnotator`](https://superverse.khulnasoft.com/latest/detection/annotators/#superverse.annotators.core.BoxAnnotator) has been removed. `BoundingBoxAnnotator` will be removed in `superverse-0.26.0`.

- `overlap_filter_strategy` in [`InferenceSlicer.__init__`](https://superverse.khulnasoft.com/latest/detection/tools/inference_slicer/) is deprecated and will be removed in `superverse-0.27.0`. Use `overlap_strategy` instead.

- `overlap_ratio_wh` in [`InferenceSlicer.__init__`](https://superverse.khulnasoft.com/latest/detection/tools/inference_slicer/) is deprecated and will be removed in `superverse-0.27.0`. Use `overlap_wh` instead.

# Removed

### 0.25.0

No removals in this version!

### 0.24.0

- The `frame_resolution_wh ` parameter in [`sv.PolygonZone`](detection/tools/polygon_zone.md/#superverse.detection.tools.polygon_zone.PolygonZone) has been removed.
- Superverse installation methods `"headless"` and `"desktop"` were removed, as they are no longer needed. `pip install superverse[headless]` will install the base library and harmlessly warn of non-existent extras.

### 0.23.0

- The `track_buffer`, `track_thresh`, and `match_thresh` parameters in [`ByteTrack`](trackers.md/#superverse.tracker.byte_tracker.core.ByteTrack) are deprecated and were removed as of `superverse-0.23.0`. Use `lost_track_buffer,` `track_activation_threshold`, and `minimum_matching_threshold` instead.
- The `triggering_position ` parameter in [`sv.PolygonZone`](detection/tools/polygon_zone.md/#superverse.detection.tools.polygon_zone.PolygonZone) was removed as of `superverse-0.23.0`. Use `triggering_anchors` instead.

### 0.22.0

- `Detections.from_khulnasoft` is removed as of `superverse-0.22.0`. Use [`Detections.from_inference`](detection/core.md/#superverse.detection.core.Detections.from_inference) instead.
- The method `Color.white()` was removed as of `superverse-0.22.0`. Use the constant `Color.WHITE` instead.
- The method `Color.black()` was removed as of `superverse-0.22.0`. Use the constant `Color.BLACK` instead.
- The method `Color.red()` was removed as of `superverse-0.22.0`. Use the constant `Color.RED` instead.
- The method `Color.green()` was removed as of `superverse-0.22.0`. Use the constant `Color.GREEN` instead.
- The method `Color.blue()` was removed as of `superverse-0.22.0`. Use the constant `Color.BLUE` instead.
- The method `ColorPalette.default()` was removed as of `superverse-0.22.0`. Use the constant [`ColorPalette.DEFAULT`](/utils/draw/#superverse.draw.color.ColorPalette.DEFAULT) instead.
- `BoxAnnotator` was removed as of `superverse-0.22.0`, however `BoundingBoxAnnotator` was immediately renamed to `BoxAnnotator`. Use [`BoxAnnotator`](detection/annotators.md/#superverse.annotators.core.BoxAnnotator) and [`LabelAnnotator`](detection/annotators.md/#superverse.annotators.core.LabelAnnotator) instead of the old `BoxAnnotator`.
- The method `FPSMonitor.__call__` was removed as of `superverse-0.22.0`. Use the attribute [`FPSMonitor.fps`](utils/video.md/#superverse.utils.video.FPSMonitor.fps) instead.

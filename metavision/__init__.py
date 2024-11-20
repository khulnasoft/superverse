import importlib.metadata as importlib_metadata

try:
    # This will read version from pyproject.toml
    __version__ = importlib_metadata.version(__package__ or __name__)
except importlib_metadata.PackageNotFoundError:
    __version__ = "development"

from metavision.annotators.core import (
    BackgroundOverlayAnnotator,
    BlurAnnotator,
    BoundingBoxAnnotator,
    BoxAnnotator,
    BoxCornerAnnotator,
    CircleAnnotator,
    ColorAnnotator,
    CropAnnotator,
    DotAnnotator,
    EllipseAnnotator,
    HaloAnnotator,
    HeatMapAnnotator,
    IconAnnotator,
    LabelAnnotator,
    MaskAnnotator,
    OrientedBoxAnnotator,
    PercentageBarAnnotator,
    PixelateAnnotator,
    PolygonAnnotator,
    RichLabelAnnotator,
    RoundBoxAnnotator,
    TraceAnnotator,
    TriangleAnnotator,
)
from metavision.annotators.utils import ColorLookup
from metavision.classification.core import Classifications
from metavision.dataset.core import (
    BaseDataset,
    ClassificationDataset,
    DetectionDataset,
)
from metavision.dataset.utils import mask_to_rle, rle_to_mask
from metavision.detection.core import Detections
from metavision.detection.line_zone import (
    LineZone,
    LineZoneAnnotator,
    LineZoneAnnotatorMulticlass,
)
from metavision.detection.lmm import LMM
from metavision.detection.overlap_filter import (
    OverlapFilter,
    box_non_max_merge,
    box_non_max_suppression,
    mask_non_max_suppression,
)
from metavision.detection.tools.csv_sink import CSVSink
from metavision.detection.tools.inference_slicer import InferenceSlicer
from metavision.detection.tools.json_sink import JSONSink
from metavision.detection.tools.polygon_zone import PolygonZone, PolygonZoneAnnotator
from metavision.detection.tools.smoother import DetectionsSmoother
from metavision.detection.utils import (
    box_iou_batch,
    calculate_masks_centroids,
    clip_boxes,
    contains_holes,
    contains_multiple_segments,
    filter_polygons_by_area,
    mask_iou_batch,
    mask_to_polygons,
    mask_to_xyxy,
    move_boxes,
    move_masks,
    oriented_box_iou_batch,
    pad_boxes,
    polygon_to_mask,
    polygon_to_xyxy,
    scale_boxes,
    xcycwh_to_xyxy,
    xywh_to_xyxy,
)
from metavision.draw.color import Color, ColorPalette
from metavision.draw.utils import (
    calculate_optimal_line_thickness,
    calculate_optimal_text_scale,
    draw_filled_polygon,
    draw_filled_rectangle,
    draw_image,
    draw_line,
    draw_polygon,
    draw_rectangle,
    draw_text,
)
from metavision.geometry.core import Point, Position, Rect
from metavision.geometry.utils import get_polygon_center
from metavision.keypoint.annotators import (
    EdgeAnnotator,
    VertexAnnotator,
    VertexLabelAnnotator,
)
from metavision.keypoint.core import KeyPoints
from metavision.metrics.detection import ConfusionMatrix, MeanAveragePrecision
from metavision.tracker.byte_tracker.core import ByteTrack
from metavision.utils.conversion import cv2_to_pillow, pillow_to_cv2
from metavision.utils.file import list_files_with_extensions
from metavision.utils.image import (
    ImageSink,
    create_tiles,
    crop_image,
    letterbox_image,
    overlay_image,
    resize_image,
    scale_image,
)
from metavision.utils.notebook import plot_image, plot_images_grid
from metavision.utils.video import (
    FPSMonitor,
    VideoInfo,
    VideoSink,
    get_video_frames_generator,
    process_video,
)

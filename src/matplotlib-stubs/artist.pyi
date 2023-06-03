from collections.abc import Callable
from typing import Any, NamedTuple

from ._typing import *
from .axes import Axes
from .backend_bases import MouseEvent, RendererBase
from .figure import Figure
from .patches import Circle, Patch, Rectangle, RegularPolygon
from .path import Path
from .patheffects import AbstractPathEffect
from .transforms import Bbox, Transform

def allow_rasterization(
    draw,
)-> Callable: ...

class _Unset:
    def __repr__(self) -> str: ...

class Artist:

    zorder: int = ...
    def __init_subclass__(cls)-> None: ...
    def __init__(self) -> None: ...
    def __getstate__(self)-> dict: ...
    def remove(self)-> None: ...
    def have_units(self)-> bool: ...
    def convert_xunits(self, x: int) -> int: ...
    def convert_yunits(self, y: int) -> int: ...
    @property
    def axes(self) -> Axes: ...
    @axes.setter
    def axes(self, new_axes: Axes): ...
    @property
    def stale(self)-> bool: ...
    @stale.setter
    def stale(self, val: bool): ...
    def get_window_extent(self, renderer: RendererBase = ...)-> Bbox: ...
    def get_tightbbox(self, renderer: RendererBase = ...) -> Bbox: ...
    def add_callback(self, func: Callable) -> int: ...
    def remove_callback(self, oid: int)-> None: ...
    def pchanged(self) -> None: ...
    def is_transform_set(self) -> bool: ...
    def set_transform(self, t: Transform) -> None: ...
    def get_transform(self) -> Transform: ...
    def get_children(self) -> list[Artist]: ...
    def contains(self, mouseevent: MouseEvent): ...
    def pickable(self) -> bool: ...
    def pick(self, mouseevent: MouseEvent)-> None: ...
    def set_picker(self, picker: bool) -> None: ...
    def get_picker(self) -> bool: ...
    def get_url(self) -> str: ...
    def set_url(self, url: str)-> None: ...
    def get_gid(self) -> str | None: ...
    def set_gid(self, gid: str) -> None: ...
    def get_snap(self) -> bool | None: ...
    def set_snap(self, snap: bool | None)-> None: ...
    def get_sketch_params(self) -> None | tuple[float, float, float]: ...
    def set_sketch_params(
        self, scale: float = ..., length: float = 128, randomness: float = 16,
    )-> None: ...
    def set_path_effects(self, path_effects: AbstractPathEffect)-> None: ...
    def get_path_effects(self) -> list[AbstractPathEffect]: ...
    def get_figure(self) -> Figure: ...
    def set_figure(self, fig: Figure)-> None: ...
    def set_clip_box(self, clipbox: Bbox)-> None: ...
    def set_clip_path(
        self,
        path: Circle | RegularPolygon | Rectangle,
        transform: Transform | None = ...,
    ) -> None: ...
    def get_alpha(self) -> float: ...
    def get_visible(self) -> bool: ...
    def get_animated(self) -> bool: ...
    def get_in_layout(self) -> bool: ...
    def get_clip_on(self) -> bool: ...
    def get_clip_box(self) -> Bbox: ...
    def get_clip_path(self) -> Path: ...
    def get_transformed_clip_path_and_affine(self): ...
    def set_clip_on(self, b: bool) -> None: ...
    def get_rasterized(self) -> bool: ...
    def set_rasterized(self, rasterized: bool) -> None: ...
    def get_agg_filter(self) -> None | Callable: ...
    def set_agg_filter(self, filter_func: Callable) -> None: ...
    def draw(self, renderer: RendererBase)-> None: ...
    def set_alpha(self, alpha: float | None) -> None: ...
    def set_visible(self, b: bool)-> None: ...
    def set_animated(self, b: bool)-> None: ...
    def set_in_layout(self, in_layout: bool)-> None: ...
    def get_label(self) -> str: ...
    def set_label(self, s: str) -> None: ...
    def get_zorder(self) -> int: ...
    def set_zorder(self, level: float) -> None: ...
    @property
    def sticky_edges(self) -> NamedTuple: ...
    def update_from(self, other: Patch) -> None: ...
    def properties(self)-> dict: ...
    def update(self, props: dict) -> list: ...
    def set(self, **kwargs) -> list | None: ...
    def findobj(self, match: Callable = ..., include_self: bool = ...) -> list: ...
    def get_cursor_data(self, event: MouseEvent)-> None: ...
    def format_cursor_data(self, data) -> str: ...
    def get_mouseover(self) -> bool: ...
    def set_mouseover(self, mouseover: bool) -> None: ...
    mouseover: property = ...

class ArtistInspector:
    def __init__(self, o: Rectangle) -> None: ...
    def get_aliases(self)-> dict: ...
    def get_valid_values(self, attr: str) -> str: ...
    def get_setters(self) -> list[str]: ...
    def is_alias(self, o)-> bool: ...
    def aliased_name(self, s: str) -> str: ...
    def aliased_name_rest(self, s: str, target)-> str: ...
    def pprint_setters(self, prop: str | None = ..., leadingspace=...) -> str|list[str]: ...
    def pprint_setters_rest(self, prop: str | None = ..., leadingspace=...)-> str|list[str]: ...
    def properties(self) -> dict[str, Any]: ...
    def pprint_getters(self) -> list[str]: ...

def getp(obj: Artist, property: str | None = ...): ...

get = getp

def setp(obj: Artist | list, *args, file: FileLike = ..., **kwargs) -> list|None: ...
def kwdoc(artist: Artist) -> str: ...
def _finalize_rasterization(draw): ...
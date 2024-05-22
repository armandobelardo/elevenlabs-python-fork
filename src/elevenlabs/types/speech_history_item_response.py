# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ..core.unchecked_base_model import UncheckedBaseModel
from .feedback_item import FeedbackItem
from .source import Source
from .speech_history_item_response_model_voice_category import SpeechHistoryItemResponseModelVoiceCategory


class SpeechHistoryItemResponse(UncheckedBaseModel):
    history_item_id: str
    request_id: typing.Optional[str] = None
    voice_id: typing.Optional[str] = None
    model_id: typing.Optional[str] = None
    voice_name: typing.Optional[str] = None
    voice_category: typing.Optional[SpeechHistoryItemResponseModelVoiceCategory] = None
    text: typing.Optional[str] = None
    date_unix: typing.Optional[int] = None
    character_count_change_from: typing.Optional[int] = None
    character_count_change_to: typing.Optional[int] = None
    content_type: typing.Optional[str] = None
    state: typing.Optional[typing.Any] = None
    settings: typing.Optional[typing.Dict[str, typing.Any]] = None
    feedback: typing.Optional[FeedbackItem] = None
    share_link_id: typing.Optional[str] = None
    source: typing.Optional[Source] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}

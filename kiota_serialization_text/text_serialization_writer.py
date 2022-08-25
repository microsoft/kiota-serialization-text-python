import base64
from datetime import date, datetime, time, timedelta
from enum import Enum
from io import BytesIO
from typing import Any, Callable, Dict, List, Optional, TypeVar
from uuid import UUID

from kiota_abstractions.serialization import Parsable, SerializationWriter

T = TypeVar("T")
U = TypeVar("U", bound=Parsable)


class TextSerializationWriter(SerializationWriter):

    NO_STRUCTURED_DATA_MESSAGE = 'Text does not support structured data'

    _on_start_object_serialization: Optional[Callable[[Parsable, SerializationWriter], None]] = None

    _on_before_object_serialization: Optional[Callable[[Parsable], None]] = None

    _on_after_object_serialization: Optional[Callable[[Parsable], None]] = None

    def __init__(self):
        self._writer: List = []

    def write_str_value(self, key: Optional[str], value: Optional[str]) -> None:
        """Writes the specified string value to the stream with an optional given key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
            value (Optional[str]): The string value to be written.
        """
        if key:
            raise Exception(self.NO_STRUCTURED_DATA_MESSAGE)
        if value:
            if self._writer:
                raise Exception(
                    'A value was already written for this serialization writer,'
                    'text content only supports a single value'
                )
            self._writer.append(value)

    def write_bool_value(self, key: Optional[str], value: Optional[bool]) -> Optional[bool]:
        """Writes the specified boolean value to the stream with an optional given key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
            value (Optional[bool]): The boolean value to be written.
        """
        if value or value is False:
            self.write_str_value(key, str(value).lower())

    def write_int_value(self, key: Optional[str], value: Optional[int]) -> Optional[int]:
        """Writes the specified integer value to the stream with an optional given key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
            value (Optional[int]): The integer value to be written.
        """
        if value:
            self.write_str_value(key, str(value))

    def write_float_value(self, key: Optional[str], value: Optional[float]) -> Optional[float]:
        """Writes the specified float value to the stream with an optional given key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
            value (Optional[float]): The float value to be written.
        """
        if value:
            self.write_str_value(key, str(value))

    def write_uuid_value(self, key: Optional[str], value: Optional[UUID]) -> Optional[str]:
        """Writes the specified uuid value to the stream with an optional given key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
            value (Optional[UUId]): The uuid value to be written.
        """
        if value:
            self.write_str_value(key, str(value))

    def write_datetime_value(self, key: Optional[str], value: Optional[datetime]) -> Optional[str]:
        """Writes the specified datetime offset value to the stream with an optional given key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
            value (Optional[datetime]): The datetime offset value to be written.
        """
        if value:
            self.write_str_value(key, str(value.isoformat()))

    def write_timedelta_value(self, key: Optional[str],
                              value: Optional[timedelta]) -> Optional[str]:
        """Writes the specified timedelta value to the stream with an optional given key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
            value (Optional[timedelta]): The timedelta value to be written.
        """
        if value:
            self.write_str_value(key, str(value))

    def write_date_value(self, key: Optional[str], value: Optional[date]) -> Optional[str]:
        """Writes the specified date value to the stream with an optional given key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
            value (Optional[date]): The date value to be written.
        """
        if value:
            self.write_str_value(key, str(value))

    def write_time_value(self, key: Optional[str], value: Optional[time]) -> Optional[str]:
        """Writes the specified time value to the stream with an optional given key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
            value (Optional[time]): The time value to be written.
        """
        if value:
            self.write_str_value(key, str(value))

    def write_collection_of_primitive_values(self, key: Optional[str],
                                             values: Optional[List[T]]) -> Optional[List[T]]:
        """Writes the specified collection of primitive values to the stream with an optional
        given key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
            values (Optional[List[T]]): The collection of primitive values to be written.
        """
        raise Exception(self.NO_STRUCTURED_DATA_MESSAGE)

    def write_collection_of_object_values(
        self, key: Optional[str], values: Optional[List[U]]
    ) -> Optional[List[Optional[Dict]]]:
        """Writes the specified collection of model objects to the stream with an optional
        given key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
            values (Optional[List[U]]): The collection of model objects to be written.
        """
        raise Exception(self.NO_STRUCTURED_DATA_MESSAGE)

    def write_collection_of_enum_values(self, key: Optional[str],
                                        values: Optional[List[Enum]]) -> Optional[str]:
        """Writes the specified collection of enum values to the stream with an optional given key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
            values Optional[List[Enum]): The enum values to be written.
        """
        raise Exception(self.NO_STRUCTURED_DATA_MESSAGE)

    def write_bytes_value(self, key: Optional[str], value: bytes) -> Optional[str]:
        """Writes the specified byte array as a base64 string to the stream with an optional
        given key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
            value (bytes): The byte array to be written.
        """
        if key and value:
            raise Exception(self.NO_STRUCTURED_DATA_MESSAGE)
        if value and not key:
            base64_bytes = base64.b64encode(value)
            base64_string = base64_bytes.decode('utf-8')
            return base64_string
        return None

    def write_object_value(self, key: Optional[str],
                           value: Optional[U]) -> Optional[Dict[Any, Any]]:
        """Writes the specified model object to the stream with an optional given key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
            value (Parsable): The model object to be written.
        """
        raise Exception(self.NO_STRUCTURED_DATA_MESSAGE)

    def write_enum_value(self, key: Optional[str], value: Optional[Enum]) -> Optional[str]:
        """Writes the specified enum value to the stream with an optional given key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
            value (Optional[Enum]): The enum value to be written.
        """
        if value:
            self.write_str_value(key, str(value.name))

    def write_null_value(self, key: Optional[str]) -> None:
        """Writes a null value for the specified key.
        Args:
            key (Optional[str]): The key to be used for the written value. May be null.
        """
        self.write_str_value(key, 'null')

    def write_additional_data_value(self, value: Dict[str, Any]) -> None:
        """Writes the specified additional data to the stream.
        Args:
            value (Dict[str, Any]): he additional data to be written.
        """
        raise Exception(self.NO_STRUCTURED_DATA_MESSAGE)

    def get_serialized_content(self) -> BytesIO:
        """Gets the value of the serialized content.
        Returns:
            BytesIO: The value of the serialized content.
        """
        text_string = ''.join(self._writer)
        self._writer = []
        stream = BytesIO(text_string.encode('utf-8'))
        return stream

    def get_on_before_object_serialization(self) -> Optional[Callable[[Parsable], None]]:
        """Gets the callback called before the object gets serialized.
        Returns:
            Optional[Callable[[Parsable], None]]:the callback called before the object
            gets serialized.
        """
        return self._on_before_object_serialization

    def get_on_after_object_serialization(self) -> Optional[Callable[[Parsable], None]]:
        """Gets the callback called after the object gets serialized.
        Returns:
            Optional[Optional[Callable[[Parsable], None]]]: the callback called after the object
            gets serialized.
        """
        return self._on_after_object_serialization

    def get_on_start_object_serialization(
        self
    ) -> Optional[Callable[[Parsable, SerializationWriter], None]]:
        """Gets the callback called right after the serialization process starts.
        Returns:
            Optional[Callable[[Parsable, SerializationWriter], None]]: the callback called
            right after the serialization process starts.
        """
        return self._on_start_object_serialization

    def set_on_before_object_serialization(
        self, value: Optional[Callable[[Parsable], None]]
    ) -> None:
        """Sets the callback called before the objects gets serialized.
        Args:
            value (Optional[Callable[[Parsable], None]]): the callback called before the objects
            gets serialized.
        """
        self._on_before_object_serialization = value

    def set_on_after_object_serialization(
        self, value: Optional[Callable[[Parsable], None]]
    ) -> None:
        """Sets the callback called after the objects gets serialized.
        Args:
            value (Optional[Callable[[Parsable], None]]): the callback called after the objects
            gets serialized.
        """
        self._on_after_object_serialization = value

    def set_on_start_object_serialization(
        self, value: Optional[Callable[[Parsable, SerializationWriter], None]]
    ) -> None:
        """Sets the callback called right after the serialization process starts.
        Args:
            value (Optional[Callable[[Parsable, SerializationWriter], None]]): the callback
            called right after the serialization process starts.
        """
        self._on_start_object_serialization = value
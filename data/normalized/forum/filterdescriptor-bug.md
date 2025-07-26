# FilterDescriptor Bug

## Question

**Tad** asked on 09 Jul 2024

Hello, I have encountered a strange bug regarding FilterDescriptor based on an Enum value. We get an automatic conversion from int32 to int16 as soon as the filter for enum is set and then the culture of a program has been changed. For example from english to german. After the culture has been changed, the enum filter that was previously set on TelerikGrid throws a cast exception as soon as we try to open it. We have fixed the problem by manually converting back from short to int, since we don't use short in our filter. However it would be great if the bug could be patched :)

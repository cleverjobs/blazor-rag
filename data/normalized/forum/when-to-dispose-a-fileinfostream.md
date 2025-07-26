# When to dispose a FileInfoStream?

## Question

**Vol** asked on 24 Jan 2025

Hi! I'm using the FileSelect component. When accessing the data, it's of type FileSelectFileInfo, which has a stream of type FileInfoStream, which is disposable. So, do I have to dispose it after having read the data? Lots of Greetings! Volker

## Answer

**Dimo** answered on 29 Jan 2025

Hi Volker, You can Close () or Dispose () our Stream and there is no problem in doing that. However, we don't explicitly require developers to do it, as it may not be necessary and it basically depends on your scenario. [https://stackoverflow.com/questions/4274590/memorystream-close-or-memorystream-dispose](https://stackoverflow.com/questions/4274590/memorystream-close-or-memorystream-dispose) [https://joeduffyblog.com/2004/12/12/follow-up-should-you-invoke-close-andor-dispose-on-a-stream/](https://joeduffyblog.com/2004/12/12/follow-up-should-you-invoke-close-andor-dispose-on-a-stream/) [https://stackoverflow.com/questions/7524903/should-i-call-close-or-dispose-for-stream-objects](https://stackoverflow.com/questions/7524903/should-i-call-close-or-dispose-for-stream-objects) On a side note, please ask the license holder at your company to assign you a license for Telerik UI for Blazor. This will make your account compliant to our license agreement. Regards, Dimo Progress Telerik

### Response

**Volker** commented on 29 Jan 2025

Many thanks! Also, I will talk to my license holder.

# FileSelect slowing down dramatically when uploading large files

## Question

**Vol** asked on 27 Jan 2025

Hi! FileSelect, when used with large files, slows down the upload speed. In my case, when going from 10MB to 100MB, upload speed goes from 2MB/s down to 300KB/s. I'm uploading into a MemoryStream with an initial capacity of the size of the file, in order to avoid reallocations. Best fit for the upload time in seconds, given the file size in MB seems to be: There seems O(n^2) complexity hidden somewhere. Does anyone know what's going on?

## Answer

**Howard** answered on 21 Feb 2025

I think while you've set an initial capacity for the MemoryStream, if the upload process involves multiple read/write operations or if the stream grows dynamically, it could lead to performance degradation. Or the size of the buffer used during the upload process can significantly impact performance. A smaller buffer size can lead to more read/write operations, which increases overhead. You should experiment with larger buffer sizes during the upload. For example, instead of uploading in small chunks, consider using a buffer in the range of 4KB to 1MB. If not already, consider using asynchronous file uploads to prevent blocking the main thread, which can improve perceived performance. geometry dash lite

### Response

**Volker** commented on 21 Feb 2025

Thank you for you reply. :-) I don't have access anymore, so for now this is purely theoretical: One more symptom I forgot to put into my initial posting is that the upload speed doesn't change over time. So, it doesn't start fast and then slows down when uploading a large file, like if resizing were going on. Large files are slow right from the start for some reason. (The buffer size for the .CopyToAsync() is the default of 128K.)

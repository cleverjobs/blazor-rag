# Save handler called multiple times for group of files?

## Question

**Bit** asked on 20 Oct 2020

Im trying to allow multiple files to be uploaded, but instead of getting all the files sent into the handler, its one at a time, at least with Chrome. What can I check? My save api handler has a signature like this [HttpPost] public async Task<IActionResult> Save(IEnumerable<IFormFile> files, string SelFileType) If I have 3 files selected for example, that method gets called 3 times each with a seperate file, instead of 1 with a collection of IFormFile objects The upload control <TelerikUpload SaveUrl="@SaveUrl" Multiple="true" OnUpload="@OnUploadHandler" OnSelect="@OnFileSelectHandler" OnError="@OnFileErrorHandler" OnSuccess="@OnSuccessHandler" />

## Answer

**Marin Bratanov** answered on 21 Oct 2020

Hi, The Save handler is called once for each file and that's expected. I have clarified this in the documentation for you ( commit link ). Regards, Marin Bratanov

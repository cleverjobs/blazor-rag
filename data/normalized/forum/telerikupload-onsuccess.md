# TelerikUpload OnSuccess

## Question

**Lou** asked on 30 Jan 2023

Hello I set Multiple="true" and I wonder if it's possible to "see" in OnSuccess event the last success upload. Or another event. I need to do something after ALL files are uploaded succefully. <TelerikUpload SaveUrl="@ImageSaveApiURL" AllowedExtensions="@AllowedFileTypes" MaxFileSize="@MaxFileSize" Multiple="true" @ref="uploadAlbumPhotosRef" OnSuccess="OnUploadSuccessHandler" OnUpload="OnFileUploadHandler"> </TelerikUpload> async Task uploadAlbumPhotosRef(UploadSuccessEventArgs e)
{
if (e.Request.Status==201)
{
var infos=new trelAlbumPhotoViewModel();

infos.Id=(Guid)Id;
infos.NomFichier=e.Request.ResponseText;

FicheEspaceClosDataService.AjouterPhotosAsync(infos);
await AfficherPhotos();
//albumPhotosRef.Rebind();
}
} Thank a lot

## Answer

**Dimo** answered on 01 Feb 2023

Hi Louis, Use the OnSelect and OnSuccess events together with some counter. OnSelect will provide the total number of selected files and then you just need to count the OnSuccess executions. Regards, Dimo

# Change error message and disable Retry button on Blazor Upload component

## Question

**Rub** asked on 02 Aug 2021

Hello Is it possible to change the error message in the Blazor Upload component to a custom error when the files get selected or uploaded? We require the files to have a specific name format, and we check for this format on the OnUpload event. We would also like to disable the retry button, because the name of the file can't be changed and thus, won't fit the naming requirement when retrying. Is this currently possible? If necessary, by using Javascript (though preferably without)? Thanks in advance. Ruben

## Answer

**Matthias** answered on 02 Aug 2021

Hi Ruben, You can change the text by localizing it: localization you will find the entry quite below: (in the example below in german) <data name="Upload_Cancel" xml:space="preserve"> <value> Abbrechen </value> </data> <data name="Upload_Clear" xml:space="preserve"> <value> Löschen </value> </data> <data name="Upload_FileStatusFailed" xml:space="preserve"> <value> Datei konnte nicht hochgeladen werden. </value> </data> <data name="Upload_FileStatusUploaded" xml:space="preserve"> <value> Datei erfolgreich hochgeladen. </value> </data> <data name="Upload_HeaderStatusUploaded" xml:space="preserve"> <value> Fertig </value> </data> <data name="Upload_HeaderStatusUploading" xml:space="preserve"> <value> Hochladen ... </value> </data> <data name="Upload_InvalidFileExtension" xml:space="preserve"> <value> Dateityp nicht erlaubt. </value> </data> <data name="Upload_InvalidMaxFileSize" xml:space="preserve"> <value> Dateigröße zu groß. </value> </data> <data name="Upload_InvalidMinFileSize" xml:space="preserve"> <value> Dateigröße zu klein. </value> </data> <data name="Upload_Remove" xml:space="preserve"> <value> Entfernen </value> </data> <data name="Upload_Retry" xml:space="preserve"> <value> Wiederholen </value> </data> <data name="Upload_SelectFiles" xml:space="preserve"> <value> Dateien auswählen... </value> </data> <data name="Upload_UploadFiles" xml:space="preserve"> <value> Hochladen </value> </data> create a class like this for example, to disable the button and assign it .cmd-not-allowed { pointer-events: none; cursor: not-allowed;
}

### Response

**Ruben** commented on 03 Aug 2021

Hello Matthias Thank you for your answer. I'll have a look at localization. But when it comes to disabling the retry button, how can I add the class to the button when evaluating the name of the file in the OnUpload event? Note that our users will usually upload multiple files at once (10+ files), and only one or two may not have the correct naming format. What I've tried before is, I added a Javascript script on my _host.html (in <Head>) as follows: <script type="text/javascript" defer> window.setRetryButtonsToDisabled=( id )=> { var selector='li[data-id="' + id + '"]'; var item=document.querySelector(selector); var buttons=item.getElementsByTagName( "button" );
buttons[ 0 ].disabled=true;
};
</script> I call this script when on Upload, but it doesn't work. When I execute this script, I get the error that item=null. protected async Task OnUploadHandler ( UploadEventArgs e ) { foreach ( var item in e.Files)
{ var errors=_templateImporter.ValidateTemplateFilename(item.Name); if (! string.IsNullOrEmpty(errors))
{
item.Status=Telerik.Blazor.UploadFileStatus.Failed;
DisableRetryButton(item.Id);
}
}
} protected async void DisableRetryButton ( string id ) { await jsRuntime.InvokeAsync<string>( "setRetryButtonsToDisabled", id);
} When I execute the code from this script in the Chrome Console debugger, it does work and it does disable the button. I understand that this is caused due to the elements I'm looking for don't exist when the page is build. But since this doesn't work, I don't know how I could add a custom class to this button if I can't get the element from the dom. Any help concerning this would be much appreciated. I understand that this is more of a Blazor/Javascript question and less of a Telerik specific question. Thanks in advance!

### Response

**Matthias** commented on 03 Aug 2021

Hello Ruben, yes, without JavaScript it will probably not work. As soon as I have time this week I will have a closer look. Best Regards

### Response

**Ruben** answered on 06 Aug 2021

I just wanted to say that I've changed the way I upload files, and now I no longer use de Telerik Upload Component, but I use the Blazor FileUpload component instead. I have more control over that component than I do with Telerik. In the future, we may return to Telerik, but for the time being, the blazor component will do. Matthias, I appreciate the help you provided!

### Response

**Matthias** commented on 06 Aug 2021

Hello Ruben, unfortunately the week was quite stressful, so I didn't really have much time. By the way, I also use the Microsoft Upload component. It's not quite as elegant visually, but allows more control and is reliable. Thanks for the feedback and have a nice weekend!

### Response

**Marin Bratanov** commented on 06 Aug 2021

I'm a tad late to the party, but what Matthias said is correct - localization is the current way to do that. Perhaps future versions will have more templates/ API for this. In the meantime, you may also want to Follow the implementation of the Telerik FileSelect component (the equivalent of the standard Upload component): [https://feedback.telerik.com/blazor/1460649-fileselect-component.](https://feedback.telerik.com/blazor/1460649-fileselect-component.)

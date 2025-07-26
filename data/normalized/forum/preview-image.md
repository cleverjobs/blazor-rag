# Preview Image

## Question

**Ton** asked on 21 May 2020

Can I priview image in onselect event ?

## Answer

**Marin Bratanov** answered on 21 May 2020

Hi Tony, You can see how you can do this here: [https://www.telerik.com/forums/upload-and-display-image-on-form](https://www.telerik.com/forums/upload-and-display-image-on-form) In OnSelect, you don't have the file because the Upload component does not send it to Blazor - this would be a performance hit for server-side blazor as ultimately the file would be sent over the wire 3 times, all of them over SignalR which is not designed for large payloads. If you want to have a file in OnSelect to modify and use immediately, you would need a FileSelect component that sends the file to the Blazor app, and not to an endpoint. In this article you can Vote for and Follow the implementation of such a Telerik component, and you can also find an example of how to make one yourself: [https://feedback.telerik.com/blazor/1460649-fileselect-component.](https://feedback.telerik.com/blazor/1460649-fileselect-component.) Regards, Marin Bratanov

### Response

**Holger** commented on 10 Mar 2022

You can do it with Javascript. In (Blazor) the OnSelect(UploadSelectEventArgs args) call a Javascript-Method I gave the fileuploader a special class (there is no id) await JS.InvokeVoidAsync( "FileHelpers.GenerateImagePreview", args.Files, UploaderClass); And then in Javascript: window.FileHelpers={ GenerateImagePreview: function ( filesNet, uploaderClass ) { var filesInput=$( '.' + uploaderClass)[ 0 ].querySelector( 'input' ).files;
FileHelpers.setup_reader(filesInput, filesNet, uploaderClass, 0 );
}, setup_reader: function ( files, filesNet, uploaderClass, i ) { var file=files[i]; var name=file.name; var reader=new FileReader();
reader.onloadend=function ( e ) {
FileHelpers.readerLoaded(e, files, filesNet, uploaderClass, i, name);
};
reader.readAsDataURL(file);
}, readerLoaded: function ( e, files, filesNet, uploaderClass, i, name ) { var id=filesNet[i].id; if (files[i][ 'type' ].split( '/' )[ 0 ]=='image' ) { var bin=e.target.result; var img=document.createElement( 'img' );
img.className="uploadPreview";
img.setAttribute( 'style', 'max-width:32px;max-height:32px;' );
img.src=bin; var wrapper=$( '.' + uploaderClass)[ 0 ];
wrapper.querySelector( '.k-file[data-id="' + id + '"] .k-file-group-wrapper' )
.replaceWith(img);
} if (i <files.length - 1 ) {
FileHelpers.setup_reader(files, filesNet, uploaderClass, i + 1 );
}
}

}; Generates the preview only for image-files and works with multiple files selected.

### Response

**Yesid** commented on 12 Jul 2022

Hello @Holger, I've tried this approach, however I get no files when selecting through JQuery var filesInput=$('.' + uploaderClass)[0].querySelector('input').files; The above yields a FileList {length: 0} result. However when I try with a simple <input type="file" id="avatar" name="avatar"> I am able to get the file once I select it. Do you have any suggestions as to why this might be?

### Response

**Holger** commented on 13 Jul 2022

Hi. I found out, there is something "special" with the Telerik Fileuploader... Have you tried your code with Firefox? In Firefox the FileList in FileElement.files is filled, in Chrome it is always empty. I started a thread in the forum about this, but with no solution. So I had to redesign my application and send the uploaded files to the server, and getting the url of the image back so I can show the preview after uploading (without the use of Javascript).

### Response

**Yesid** commented on 13 Jul 2022

Hi @Holger, That's unfortunate. I will have to use the same approach in that case. Thank you!

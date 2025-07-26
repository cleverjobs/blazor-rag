# Add icon to the dialog title and dialog buttons (Predefined Dialogs)

## Question

**Val** asked on 09 Aug 2022

I'm using the "Predefined Dialogs".... await Dialogs. ConfirmAsync ( "Are you sure?", Title ); How can I add icon to the dialog title and dialog buttons

## Answer

**Dimo** answered on 10 Aug 2022

Hello Valeriy, It's technically possible to add icons to the predefined icons, BUT: It's hackish Not flexible and customizable per Dialog instance Will affect all Dialogs in the app That's why I recommend using the non-predefined Dialogs instead. The example below is more of a front-end challenge out of curiosity, rather than a real-world use case. <TelerikButton OnClick="@ShowConfirmWithTitle">Show Confirm</TelerikButton> <style> /* common preparation for Dialog icons */.k-dialog.k-dialog-title::before,.k-dialog.k-dialog-content::before,.k-dialog.k-dialog-buttongroup.k-button::before { display: inline-block; width: 16px; height: 22px; font-size: 16px; font-family: WebComponentsIcons; vertical-align: middle; position: static; opacity: 1; background: none transparent;
} /* icon in Dialog title */.k-dialog.k-dialog-title::before { content: "\e402"; margin-right: . 5em;
} /* icon in Dialog content */.k-dialog.k-dialog-content::before { content: "\e402"; margin-right: . 2em;
} /* icon in Dialog non-primary button */.k-dialog.k-dialog-buttongroup.k-button::before { content: "\e115";
} /* icon in Dialog primary button */.k-dialog.k-dialog-buttongroup [class*=primary]::before { content: "\e118";
} </style> @code {
[CascadingParameter] public DialogFactory Dialogs { get; set; } async Task ShowConfirmWithTitle ( ) {
bool isConfirmed=await Dialogs.ConfirmAsync( "Are you sure?", "Confirmation" );
}
} Regards, Dimo

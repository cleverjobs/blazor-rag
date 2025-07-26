# Predefine dialogs don't show buttons text

## Question

**Bla** asked on 22 Jun 2021

Hi all. I've a simple confirm dialogue routine. I follow the examples in the documentation. The code looks like: protected async void OnNHibernateLogsChange ( ) { bool confirm=await ActivateFilterConfirm(); // ask about if (confirm || _showNHibernateLogs==false )
{
LoggerConfig.FilterNHibernateLogs=!_showNHibernateLogs; string msg=_showNHibernateLogs ? L10n[ "NM-SHOWNHIBLOGS" ] : L10n[ "NM-HIDENHIBLOGS" ];
NotificationManager.ShowInfo(msg);
} else {
_showNHibernateLogs=!_showNHibernateLogs;
}
} The problem is that the dialog box buttons don't have a text. It is not an styles issue. I've inspected and the generated div is empty. Any ideas on what is going on? Thanks.

## Answer

**Blazorist** answered on 24 Jun 2021

Copy & paste the documentation example. Same result: no text in buttons. See image below: Someone have the same problem? Support team?

### Response

**Blazorist** commented on 28 Jun 2021

Almost one week and no response.

### Response

**Mario** commented on 18 Oct 2021

I'm having the same problem with Dialogs.ConfirmAsync("Are you sure?", "Delete Item"); And if I use the default delete confirmation of a telerik grid Mario

### Response

**Mario** commented on 18 Oct 2021

I'm using localization... If I comment the localization code in Program.cs the text will be shown How can I solve this issue?

### Response

**Mario** answered on 19 Oct 2021

I solved setting in the localization files these resources: Dialog_Cancel and Dialog_Ok.

### Response

**Dimo** commented on 21 Oct 2021

Hello Mario, We intend to enhance the Dialog component in early 2022 to allow full content customization, without the need to use localization. Follow this feature request to receive status updates.

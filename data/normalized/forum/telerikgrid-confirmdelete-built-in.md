# TelerikGrid ConfirmDelete Built-In

## Question

**Gin** asked on 23 Mar 2022

Is there a way to override the built in message (Are you sure you want to delete this record?) when setting TelerikGrid ConfirmDelete to true? I'd prefer not creating a new instance of dialog to achieve this. Thanks.

## Answer

**Marin Bratanov** answered on 26 Mar 2022

Hello Gino, You can use localization for this - check the Grid_ConfirmDeleteText string (and perhaps the other Grid_Confirm* strings if needed, such as the title one). Regards, Marin Bratanov

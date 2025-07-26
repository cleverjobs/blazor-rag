# ComboBox bind-Value

## Question

**Gia** asked on 13 Apr 2020

Hi I've put a TelerikComboBox inside a TelerikWindow not visible by default. <TelerikComboBox Data="@ListaUnMis" Filterable="false" Placeholder="Selezione Unotà di Misura" @bind-Value="@selectedProduct.CodUnMis" TextField="@nameof(CMD_UnMis.Descrizione)" ValueField="@nameof(CMD_UnMis.CodUnMis)" AllowCustom="false"> </TelerikComboBox> In a grid when I click an edit button I open the modal TelerikWindow and set the selectedProduct. ...but .... the inital valu is not displayed. Remain only blank. Using TelerikDropDownList all works fine. Tnx

## Answer

**Marin Bratanov** answered on 14 Apr 2020

Hi Giampaolo, Can you confirm you have upgraded to 2.10.0? There was an issue in 2.9.0 with the selected text of the combo box that has been fixed. I am also attaching here a simple component I built on top of this code that seems to work on my end so you can test it with 2.10.0 to see if it works for you. If not, please post here the modification that will break it. Regards, Marin Bratanov

### Response

**Giampaolo** answered on 14 Apr 2020

Really tnx Upgrading to 2.1 now works tnx

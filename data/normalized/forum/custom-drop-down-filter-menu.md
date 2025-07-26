# Custom Drop-Down Filter Menu

## Question

**AliAli** asked on 06 Jan 2024

I need sample Drop-Down custom filter menu for this Grid, i dont see sample in telerik docs <GridColumn Field="MoneyTransferCode" FieldType=" @( typeof ( int ) ) " Title=" نوع انتقال وجه " Width="200px" Groupable="true"> <GroupHeaderTemplate> نوع انتقال وجه: @Data. Where (x=> x. MoneyTransferCode==int. Parse (context. Value. ToString ())). Select (x=> x. MoneyTransferCodeName ). FirstOrDefault () </GroupHeaderTemplate> <Template> @{ var item=context as TermOfTransactionDto; @item. MoneyTransferCodeName } </Template> <EditorTemplate> @{ var item=context as TermOfTransactionDto; <TelerikDropDownList Data=" @MoneyTransferCodeList " ValueField="Value" TextField="PersianDisplayName" Width="100%" @bind-Value=" @item. MoneyTransferCode " /> } </EditorTemplate> </GridColumn>

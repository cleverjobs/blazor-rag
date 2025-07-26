# Grid with SplitButton in GridColumnTemplate

## Question

**Mat** asked on 27 Sep 2024

I have a grid and I want to present the user with a set of custom actions for each specific row. I am using the splitbutton control in the gridcolumn template. The grid and splitbutton renders but the splitbutton popup is not visible. [https://blazorrepl.telerik.com/mykXmBPX33zR9mDO27](https://blazorrepl.telerik.com/mykXmBPX33zR9mDO27) <TelerikGrid Data="@data">
<GridColumns>
<GridColumn>
<Template>
<TelerikSplitButton Icon="@SvgIcon.FileExcel">
<SplitButtonContent />
<SplitButtonItems>
<SplitButtonItem Icon="@SvgIcon.FilePdf" />
<SplitButtonItem Icon="@SvgIcon.DataJson" />
</SplitButtonItems>
</TelerikSplitButton>
</Template>
</GridColumn>
<GridColumn Field="@nameof(Data.field)" />
</GridColumns>
</TelerikGrid>

@code { class Data { public string field{ get; set; }
}

IEnumerable<Data> data=Enumerable.Range( 0, 10 ).Select(x=> new Data { field=x.ToString() });
}

## Answer

**Hristian Stefanov** answered on 29 Sep 2024

Hi Matt, The reason the SplitButton popup isn't appearing is that each <SplitButtonItem> tag needs to have some content. If you prefer not to use text, you can include a TelerikSvgIcon as the content. I've modified your example with these changes: REPL link. Please run and test it to see the updated result. Regards, Hristian Stefanov Progress Telerik

### Response

**Matt** commented on 30 Sep 2024

Thanks that worked!

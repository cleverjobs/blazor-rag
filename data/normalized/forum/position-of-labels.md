# Position of Labels

## Question

**Pet** asked on 29 Nov 2020

Hi, the labels 'Start' and 'End' of the TelerikDateRangePicker are shown over the input controls. Example Razor page: @page "/Testsupport1" <TelerikToolBar> <ToolBarTemplateItem><label for="cbId">Label1</label></ToolBarTemplateItem> <ToolBarTemplateItem> <TelerikComboBox TItem="string" TValue="string" Width="80px" Id="cbId" /> </ToolBarTemplateItem> <ToolBarButton Icon="refresh">Refresh</ToolBarButton> <ToolBarTemplateItem> <label for="ddlId">Label2</label> </ToolBarTemplateItem> <ToolBarTemplateItem> <TelerikDropDownList TItem="string" TValue="string" Id="ddlId" Width="80px" /> </ToolBarTemplateItem> <ToolBarTemplateItem> <TelerikDateRangePicker T="DateTime" /> </ToolBarTemplateItem> </TelerikToolBar> Image: [https://imgur.com/S0fiwRq](https://imgur.com/S0fiwRq) How can I adjust the position of labels and controls? It is ok to show the labels above, but then for all controls. Or how can I modify TelerikDateRangePicker to use one line and show the labels before the controls. Best Regards, Peter

## Answer

**Svetoslav Dimitrov** answered on 02 Dec 2020

Hello Peter, By the design, the labels for the DateRangePicker are above it. You could use some CSS to move them to the right of the date inputs (to the on the same line). I have made a Knowledge Base article, which you could see from this link, which explains how to achieve that. Regards, Svetoslav Dimitrov

### Response

**Peter** answered on 02 Dec 2020

Hello Svetoslav, thanks, but the labels for the Combo/DrobpdownBox are to high yet. I have to add it to the css selector. <style> .reposition-labels .k-floating-label-container { padding-top: 0; width: auto; flex-direction: row-reverse; align-items: center; } label.reposition-labels, .reposition-labels .k-floating-label-container> .k-label { position: static; margin: 0 .5em; } </style> <TelerikToolBar> <ToolBarTemplateItem><label for="cbId" class="reposition-labels">Label1</label></ToolBarTemplateItem> <ToolBarTemplateItem> <TelerikComboBox TItem="string" TValue="string" Width="80px" Id="cbId" /> </ToolBarTemplateItem> <ToolBarButton Icon="refresh">Refresh</ToolBarButton> <ToolBarTemplateItem> <label for="ddlId" class="reposition-labels">Label2</label> </ToolBarTemplateItem> <ToolBarTemplateItem> <TelerikDropDownList TItem="string" TValue="string" Id="ddlId" Width="80px" /> </ToolBarTemplateItem> <ToolBarTemplateItem> <div class="reposition-labels"> <TelerikDateRangePicker T="DateTime" /> </div> </ToolBarTemplateItem> </TelerikToolBar> Regards, Peter

### Response

**Svetoslav Dimitrov** answered on 03 Dec 2020

Hello Peter, To align the labels for the DropDownLIst and the ComboBox you should remove the 0.5em margin bottom. I have made an example, where you could see how I did it. Since I answered your question in this thread I will close your other forum post. <style>.configure-input-labels { margin-bottom: 0px;
}
</style>

<TelerikToolBar>
<ToolBarTemplateItem>
<label for=" cbId " class=" configure-input-labels "> Label1 </label>
<TelerikComboBox TItem=" string " TValue=" string " Width="80 px " Id=" cbId " />
</ToolBarTemplateItem>
<ToolBarButton Icon=" refresh "> Refresh </ToolBarButton>
<ToolBarTemplateItem>
<label for=" ddlId " class=" configure-input-labels "> Label2 </label>
<TelerikDropDownList TItem=" string " TValue=" string " Id=" ddlId " Width="80 px " />
</ToolBarTemplateItem>
<ToolBarTemplateItem>
<div class=" reposition-labels ">
<TelerikDateRangePicker T=" DateTime " />
</div>
</ToolBarTemplateItem>
</TelerikToolBar> Regards, Svetoslav Dimitrov

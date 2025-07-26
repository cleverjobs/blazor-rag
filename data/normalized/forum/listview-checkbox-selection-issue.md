# Listview Checkbox Selection Issue

## Question

**Vis** asked on 25 Jan 2021

when I am selecting the checkbox value and the another checkbox also selected. Please see attached file <TelerikListView Data="@editModel.Groups" Height="200px"> <Template Context="dlcontext"> <div class="row" style="margin-left:0px; margin-right:0px;"> <div class="col-12 mt-sm" style="margin-top: 3px; margin-bottom: 3px;"> <label for="@dlcontext.Name"> <TelerikCheckBox @bind-Value="@editModel.IsSelected" Id="@dlcontext.Name" Enabled="true" /> @dlcontext.Name </label> </div> </div> </Template> </TelerikListView> Thanks, Vishnu Vardhanan

## Answer

**Nadezhda Tacheva** answered on 26 Jan 2021

Hi Vishnu, The parameter that is responsible for the state of the checkbox (whether it is checked or unchecked) is the Value parameter. In the current setup it is bound to the IsSelected field from the model, it does not use the IsSelected field of the context of the separate checkboxes. <TelerikCheckBox @bind-Value="@editModel.IsSelected" Id="@dlcontext.Name" Enabled="true" /> When you check one checkbox, all of them get checked because they actually have the same value received form the model. To achieve the desired behavior, bind the checkbox value to the IsSelected field of the context (dlcontext), so it will reflect the value according to the current element (see below). <TelerikCheckBox @bind-Value="@dlcontext.IsSelected" Id="@dlcontext.Name" Enabled="true" /> Regards, Nadezhda

### Response

**Vishnu** answered on 28 Jan 2021

Thank You Nadezhda, Its Working Fine...

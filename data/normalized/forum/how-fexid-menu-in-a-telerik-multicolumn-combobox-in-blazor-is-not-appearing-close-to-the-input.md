# how fexid menu in a Telerik MultiColumn ComboBox in Blazor is not appearing close to the input

## Question

**bas** asked on 04 Oct 2023

</di v> <div class="row"> <div class="col-md-6"> <div class="row"> <div class="col-md-3 col-lg-3 col-xs-12"> <label for="Year-select" class="k-label k-form-label">QuestionNumber </label> </div> <div class="col-md-8 col-lg-8 col-xs-12"> <TelerikMultiColumnComboBox Value="@Parameter.Id" Id="Year-select" ScrollMode="@DropDownScrollMode.Virtual" Data="@Data" ValueField="@(nameof(Model.Id))" TextField="@(nameof(Model.Description))" Width="75%" PageSize="30" ItemHeight="35" Filterable="true" FilterOperator="@Telerik.Blazor.StringFilterOperator.Contains" ListHeight="260px" Placeholder="New"> <MultiColumnComboBoxColumns> <MultiColumnComboBoxColumn Title="Description" Field="@nameof(Model.TextMajorDescription)" /> </MultiColumnComboBoxColumns> </TelerikMultiColumnComboBox> <TelerikLoader Class="loader-indicator" ThemeColor="light"></TelerikLoader> </div> </div> </div>

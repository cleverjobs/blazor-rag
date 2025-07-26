# Is there a way when I focus on TelerikDatePicker field the numeric keypad is automatically displayed

## Question

**Has** asked on 22 Apr 2025

I am working on a mobile app using Blazor Hybrid, I have a TelerikDatePicker field on a page. Is there a practical way when I focus on that field it automatically shows the numeric keyboard instead of alphanumeric keyboard ? like when using TelerikNumericTextBox. Thank you.

## Answer

**Anislav** answered on 22 Apr 2025

Yes, you can control the type of virtual keyboard by setting the InputMode parameter of the TelerikDatePicker to "decimal" or "numeric". Edit: Note that this parameter was recently introduced in version 8.0 – Telerik UI for Blazor 8.0.0 (2025 Q1). Regards, Anislav Atanasov

### Response

**Hassan** commented on 22 Apr 2025

Hi Atanasov,, First of all thank you for a quick response. When you use TelerikDatePicker 'InputMode' property you get the following Exception: TelerikDatePicker does not have a property matching the name 'InputMode' This is my code: <TelerikForm Model="@m_oPatientSearch" @ref="m_oPatientSearchForm2" OnValidSubmit="@OnSubmitForm2PatientSearch" Class="search-form"> <FormValidation> <DataAnnotationsValidator></DataAnnotationsValidator> </FormValidation> <FormItems> <div class="mt-0 form-group"> <FormItem Field="@nameof(m_oPatientSearch.PolySearchData.Name)"> <Template> <div class="mb-1"> <TelerikTextBox @ref="@m_oNameTextBoxRef" Placeholder="@m_oLocalizer!["ExternPolyclinicView_SearchPatient_Name_Placeholder"]" Class="@m_sTextBoxNameStyle" @bind-Value="@m_oPatientSearch!.PolySearchData!.Name" Autocomplete="off" DebounceDelay="0"></TelerikTextBox> </div> </Template> </FormItem> <FormItem Field="@nameof(m_oPatientSearch.PolySearchData.DateOfBirth)"> <Template> <div class="mb-1"> <TelerikDatePicker @ref="@m_oDatePickerRef" Class="@m_sDatePickerDOBStyle" InputMode="numeric" @bind-Value="@m_oDateOfBirth" Format="dd-MM-yyyy" Min="@m_dtDatePickerMin" Max="@m_dtDatePickerMax" Width="100%"> <HeaderTemplate> <span> <TelerikButton OnClick="@GoToPrevious" Icon="@SvgIcon.ArrowLeft" Title="Go to Previous Month" Size="@ThemeConstants.Button.Size.Small" /> <TelerikButton OnClick="@SelectToday" Size="@ThemeConstants.Button.Size.Small">@m_oLocalizer!["Common_DatePicker_Btn_Today_Text"]</TelerikButton> <TelerikButton OnClick="@GoToNext" Icon="@SvgIcon.ArrowRight" Title="Go to Next Month" Size="@ThemeConstants.Button.Size.Small"></TelerikButton> </span> <span style="padding-right: .6em;"> @m_dtDatePickerViewDate.ToString("MMM") <TelerikNumericTextBox Value="@m_dtDatePickerViewDate.Year" ValueChanged="@NumericTextBoxValueChanged" T="@int" Min="@m_iNumericTextBoxMin" Max="@m_iNumericTextBoxMax" Width="6em" Size="@ThemeConstants.NumericTextBox.Size.Small" /> </span> </HeaderTemplate> </TelerikDatePicker> </div> </Template> </FormItem> <FormItem Field="@nameof(m_oPatientSearch.PolySearchData.City)"> <Template> <div class="k-form-field-wrap"> <TelerikDropDownList @bind-Value="@m_oPatientSearch.PolySearchData!.City" Class="@m_sDropDownCityStyle" Id="city" Data="@m_lstAvailableAreas" DefaultText="@m_oLocalizer!["ExternPolyclinicView_SearchPatient_City_Groupbox"]" TItem="string" TValue="string" Filterable="@m_bFilterable" FilterOperator="@m_oFilterOperator" FilterDebounceDelay="@m_iFilterDebounceDelay" FilterPlaceholder="@m_sFilterPlaceholder"> <NoDataTemplate> <div> <TelerikSvgIcon Icon="@SvgIcon.InfoCircle" Size="@ThemeConstants.SvgIcon.Size.Large" /> <br /> <br /> <span class="app-font-style text-muted">@m_oLocalizer!["Common_DropDown_No_Items_Message"]</span> </div> </NoDataTemplate> </TelerikDropDownList> </div> </Template> </FormItem> </div> </FormItems> <FormButtons> <CardSeparator></CardSeparator> <CardActions Layout="@CardActionsLayout.Center"> <div class="text-center mt-0 mb-0"> <TelerikButton ButtonType="@ButtonType.Submit" Enabled="@m_bEnable" Icon="@SvgIcon.Search" Class="app-std-btn"> @m_oLocalizer!["ExternPolyclinicView_Search"] </TelerikButton> </div> </CardActions> </FormButtons> </TelerikForm>

### Response

**Anislav** commented on 22 Apr 2025

Which version of Telerik UI for Blazor are you using? I believe InputMode wasn't available in older versions. Regards, Anislav Atanasov

### Response

**Hassan** commented on 22 Apr 2025

We use Telerik.UI.for.Blazor (6.2.0) Regards, Hassan

### Response

**Anislav** commented on 22 Apr 2025

The parameter was recently introduced in version 8.0 – Telerik UI for Blazor 8.0.0 (2025 Q1). I’ve updated my answer to reflect that. You’ll need to update the version you're using in order to take advantage of the InputMode parameter.

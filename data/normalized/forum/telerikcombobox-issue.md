# TelerikCOmbobox issue

## Question

**ste** asked on 09 Mar 2022

Hi, I have a combobox loaded with databse values, and I want to set the selected value with the value of my selected record when I open my telerikwindow where my combobox is. Right now it doesn't work. .razor <FormItem ColSpan="1"> <Template> <label for="store-country" class="k-label k-form-label">Pays</label> <TelerikComboBox Data="@CountryList" TextField="DescFr" ValueField="Id" @bind-Value="@SelectedCountryId" Width="90%"></TelerikComboBox> </Template> </FormItem> .cs public void StoreEdit(int storeSelected=0) { SetDropDownList(); if (storeSelected> 0) { store=storeService.ReadItem(storeSelected); SetSelectedValue(store); } } private void SetSelectedValue(RSS_BasicStoreNational store) { SelectedProvinceId=store.IDProvince; SelectedCountryId=store.IDCountry; SelectedRegionId=store.RegionID; SelectedDistChannelId=store.DistributionChannel; SelectedInStoreSystemCode=store.CodeInStoreSystem; SelectedStoreTypeId=store.StoreTypeID; SelectedLanguageCode=store.CodeLanguage; OpenDateTimePicker=store.OpeningDate !=null ? store.OpeningDate.Value : DateTime.Today; if (store.ClosingDate !=null) CloseDateTimePicker=store.ClosingDate; } private void SetDropDownList() { ProvinceList=storeService.GetProvinces(); CountryList=storeService.GetCountries(); RegionList=storeService.GetRegions(); DistChannelList=storeService.GetDistChannels(); InStoreSystemList=storeService.GetInStoreSystems(); StoreTypeList=storeService.GetStoreTypes(); LanguageList=storeService.GetLanguages(); }

### Response

**Marin Bratanov** commented on 12 Mar 2022

Could you add some more context on the situation - when are these methods called, is there data in the combo box before that, are you using the latest UI for Blazor version? Editing the sample to be runnable (you could even post a simplified one with dummy hardcoded via the REPL runner ) will help a lot.

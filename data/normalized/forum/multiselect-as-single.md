# Multiselect as single

## Question

**Ila** asked on 26 Feb 2023

I'm using this syntax: <TelerikMultiSelect Class="searchSurveyor" ClearButton="true" OnRead="ReadItems" Filterable="true" Placeholder="Search Surveyor" OnChange="SetSurveyors" Width="100%" Data="@_surveyorsData" TextField="TextField" ValueField="ValueField" @bind-Value="_selectedSurveyorsData"> </TelerikMultiSelect> I want to make it act like a single select where the last selected value replaces the first. But manipulating the bind-value doesn't seem to help private async void SetSurveyors ( object theUserInput ) { if (theUserInput==null ) return;

_selectedSurveyorsData=(List<string>)theUserInput; if (_selectedSurveyorsData.Count> 1 )
{
_selectedSurveyorsData[ 0 ]=_selectedSurveyorsData[ 1 ];
_selectedSurveyorsData.RemoveAt( 1 );
}

} Any idea?

## Answer

**Ivan** answered on 27 Feb 2023

Hello, IIan! It's very simple: [https://blazorrepl.telerik.com/mHOGwBPs543JSkgP16](https://blazorrepl.telerik.com/mHOGwBPs543JSkgP16)

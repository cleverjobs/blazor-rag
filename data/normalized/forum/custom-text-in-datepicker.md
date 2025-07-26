# Custom Text In DatePicker

## Question

**Moh** asked on 07 Jan 2025

Hello I want to display the desired text in the DatePicker after selecting the date from TelerikDatePicker. Currently, after selecting the DatePicker, the date is displayed in this field, to which I want to add the desired text. For example, in the DatePicker field after selecting the date, instead of 07/01/2025 , today is 07/01/2025. If it is not possible to change the text, at least no text should be displayed in the DatePicker after selecting the date. Please help me. Code and image: <TelerikDatePicker @bind-Value="DatePickerValue">
</TelerikDatePicker>

@code { private DateTime DatePickerValue { get; set; }=DateTime.Today;
{

## Answer

**Hristian Stefanov** answered on 08 Jan 2025

Hi Mohamad, You can achieve the desired result with some CSS positioning. I've prepared an example below, and depending on your business needs you might need to adjust the pixel values to suit your specific requirements. <style> /* Wrapper container for positioning */.datepicker-container { position: relative; display: inline-block;
} /* Style the input field and create space for the "Today is" text */.k-datepicker input { margin-left: 55px; /* Create space inside the input for the text */ font-size: 14px;
} /* Position the "Today is" text inside the input */.today-text { position: absolute; top: 50%; left: 10px; /* Adjust to position the text inside the input */ transform: translateY (- 50% ); /* Vertically center the text */ font-size: 14px; font-weight: normal;
} </style> <div class="datepicker-container"> <TelerikDatePicker @bind-Value="DatePickerValue" Width="300px"> </TelerikDatePicker> <div class="today-text"> Today is </div> </div> @code {
private DateTime DatePickerValue { get; set; }=DateTime.Today;
} Regards, Hristian Stefanov Progress Telerik

### Response

**Mohamad Javad** commented on 08 Jan 2025

Hello Thank you The problem is solved. I also wrote a code that could be another solution: <TelerikDatePicker @bind-Value="DatePickerValue" Format="@format" OnClose="@OnBlurHandler">
</TelerikDatePicker>

@code { private DateTime DatePickerValue { get; set; }=DateTime.Today; public string format; private void OnBlurHandler () {
format="Custom " +@DatePickerValue.ToShortDateString();
}
} Thanks

### Response

**Hristian Stefanov** commented on 09 Jan 2025

Hi Mohamad, I’m glad to hear that the solution from my first message resolved your problem. As for the second option involving the Format parameter, it’s not a valid alternative because the format must adhere to the standard date formats supported in C#. Therefore, I recommend sticking with the CSS approach. Kind Regards, Hristian

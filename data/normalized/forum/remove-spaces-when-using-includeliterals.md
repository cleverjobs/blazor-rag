# Remove spaces when using IncludeLiterals

## Question

**Hum** asked on 02 Jul 2024

Hi, I use TelerikMaskedTextBox with IncludeLiterals, but the value is always padded with spaces to the mask's length. Is there a way to trim the value? For example, if I have a partially filled phone mask, I can't determine whether it is valid based on the length. Also, when stored in the database, having those spaces can be an issue when used by another method in the application. Thanks,

## Answer

**Tsvetomir** answered on 05 Jul 2024

Hi Humberto, To handle this scenario, use the ValueChanged event to validate the input value based on the mask length by using the String.Trim Method. Here, I'm sending you an example that demonstrates this approach: <TelerikMaskedTextBox Mask="(+999) 000-0000" Value="@TheValue" ValueChanged="@((string newValue)=> ValidateInput(newValue))" IncludeLiterals="@ShouldAddLiterals"> </TelerikMaskedTextBox> Is valid: @IsValid.ToString() <span style="white-space: pre;background:yellow"> @TheValue </span> <label> <input type="checkbox" @bind="@ShouldAddLiterals" /> Include literals </label> @code {
string TheValue { get; set; }
bool ShouldAddLiterals { get; set; }=true; bool IsValid { get; set; } private void ValidateInput(string newValue)
{ IsValid=newValue.Trim().Length==(ShouldAddLiterals ? 15 : 10); TheValue=newValue;
} On a side note, if the above approach does not align with your requirements and the goal is to remove whitespaces before input validation, you can use the String.Replace Method to replace the whitespaces with an empty string. However, please note that this approach has a drawback: when a user tries to fill the input in a non-standard way, such as from back to front, the whitespaces are deleted, and the characters shift to the first missing position. I hope the provided information helps you to move forward with you requirements. Regards, Tsvetomir Progress Telerik

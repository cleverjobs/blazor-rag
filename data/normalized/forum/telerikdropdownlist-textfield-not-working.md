# TelerikDropDownList TextField not working

## Question

**Lor** asked on 24 Sep 2024

I have a very simple scenario with a TelerikDropDownList, like the following: <TelerikDropDownList Data="@foundComponents" @bind-Value="@componentId" ValueField="ComponentId" TextField="Description"> </TelerikDropDownList> Then, I have declared the required properties and then there is my method that loads the data in the "foundComponents" collection. @code { protected string? componentId; protected IEnumerable<Component>? foundComponents;

... private async Task SearchComponentAsyncHandler () {
foundComponents=( await JsonSerializer.DeserializeAsync<ZollerBrowseResult>(responseStream)).BrowseResult?.Select(x=> x.Component);
}
} and this is my "ZollerBrowseResult" model and its related classes: public class ZollerBrowseResult { public required BrowseResult[]? BrowseResult { get; set; }
} public class BrowseResult { public required Component Component { get; set; }
} public class Component { public string? ComponentId { get; set; }
[ JsonPropertyName( "Component.ComponentId" ) ] private string Component_ComponentId { set { ComponentId=value; } } public string? Description { get; set; } public Article? Article { get; set; }
} For some reason, when I run the application, the Dropdown doesn't show the Description property, it shows the class FullName instead. I don't understand what I am doing wrong here.

## Answer

**Lorenzo** answered on 25 Sep 2024

My bad, my "foundComponents" collection was wrongly populated.

### Response

**Hristian Stefanov** commented on 25 Sep 2024

Hi Lorenzo, I'm glad to hear that you have quickly resolved the matter on your own. Thank you for sharing how things turned out publicly so other developers in the same situation can benefit from this. Kind Regards, Hristian

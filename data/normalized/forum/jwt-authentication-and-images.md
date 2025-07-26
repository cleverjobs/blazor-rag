# JWT authentication and images

## Question

**Rém** asked on 11 Jun 2020

Hi, My app needs authentication and I use JWT. Is want to populate a TreeView with some personal image, but the question stay open for all component with ImageUrlField property How to query an image url that contains the JWT token, ie in the header Authorization: Bearer <token> ? Thanks

## Answer

**Marin Bratanov** answered on 11 Jun 2020

Hello Rémi, How would you use an <img /> tag and include this token in your app? I am not aware of a built-in way to do that and at this point my best suggestion is that you implement a Razor Component that provides this capability as required by your situation, and use it in a template in the Telerik component (link to the treeview templates examples ). Regards, Marin Bratanov

### Response

**Rémi** answered on 13 Jun 2020

Thanks Marin, The work around I found is to use HttpClient to download the image stream and set URL like this string urlField { get { ... HttpClient logic here ... string imageBase64Data=Convert.ToBase64String(ms.ToArray()); return string.Format("data:image/jpeg;base64,{0}", imageBase64Data); } } Rémi

### Response

**Marin Bratanov** answered on 13 Jun 2020

Hello Rémi, I expected this would be the general approach. I have marked your post as an answer to this thread. Regards, Marin Bratanov

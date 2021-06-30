### AzureAppServiceCLI

## Tạo Domain Azure nhanh

- Ở Portal Azure chọn cloudshell ở bên phải thanh tìm kiếm sau đó chọn BASH
- Nếu có nhiều sub thì phải chọn sub đó:
```shell
az account set --subscription <name>
```

- Tải file contact json:
```shell
 wget https://raw.githubusercontent.com/haku1806/AzureAppServiceCLI/main/AppServiceDomain/contact_info.json -O contact.json
```
 
- Chạy lệnh tạo domain theo ý bạn:
```shell
az appservice domain create -g your-group-resource --hostname your-domain --contact-info=@'contact.json' --accept-terms
```

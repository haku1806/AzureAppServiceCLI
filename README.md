### AzureAppServiceCLI

## Tạo Domain Azure nhanh

- Ở Portal Azure chọn cloudshell ở bên phải thanh tìm kiếm sau đó chọn BASH
- Nếu có nhiều sub thì phải chọn sub đó:
```bash
az account set --subscription 'name'
```

- Tải file contact json:
```bash
 wget https://raw.githubusercontent.com/haku1806/AzureAppServiceCLI/main/AppServiceDomain/contact_info.json -O contact.json
```
 
- Chạy lệnh tạo domain theo ý bạn:
```bash
az appservice domain create -g your-group-resource --hostname your-domain --contact-info=@'contact.json' --accept-terms
```

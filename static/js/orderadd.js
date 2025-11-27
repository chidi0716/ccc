// 開啟與關閉Modal
function open_input_table() {
    document.getElementById("addModal").style.display = "block";
}
function close_input_table() {
    document.getElementById("addModal").style.display = "none";
}

function delete_data(value) {
    // 發送 DELETE 請求到後端
    fetch(`/product?order_id=${value}`, {
        method: "DELETE",
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("伺服器回傳錯誤");
            }
            return response.json(); // 假設後端回傳 JSON 格式資料
        })
        .then(result => {
            console.log(result); // 在這裡處理成功的回應
            close_input_table(); // 關閉 modal
            location.assign('/'); // 重新載入頁面
        })
        .catch(error => {
            console.error("發生錯誤：", error);
        });
}

// 1. 選取商品種類後的連動邏輯 (Fetch API)
function selectCategory() {
    const category = document.getElementById("category").value;
    const productSelect = document.getElementById("product-name");

    // Clear existing options
    productSelect.innerHTML = '<option value="" disabled selected>請選擇商品</option>';

    fetch(`/product?category=${category}`)
        .then(response => response.json())
        .then(data => {
            data.product.forEach(product => {
                const option = document.createElement("option");
                option.value = product;
                option.text = product;
                productSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching products:', error));
}

// 2. 選取商品後的價格更新邏輯 (Fetch API)
function selectProduct() {
    const productName = document.getElementById("product-name").value;

    fetch(`/product?product=${productName}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("product-price").value = data.price;
            countTotal();
        })
        .catch(error => console.error('Error fetching price:', error));
}

// 3. 計算小計邏輯
function countTotal() {
    const price = parseFloat(document.getElementById("product-price").value) || 0;
    const amount = parseInt(document.getElementById("product-amount").value) || 0;
    const total = price * amount;
    document.getElementById("product-total").value = total;
}
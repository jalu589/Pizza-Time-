function addToOrder(type, item) {
    console.log('add', type, item)
    if (type == 'cookie') {
        console.log('cookie')
    }
    else {
        let size = document.querySelector(`#size-${type}-${item}`).value
        console.log(size)
        let quantity = document.querySelector(`#quantity-${type}-${item}`).value
        console.log(quantity)
        
    }

}
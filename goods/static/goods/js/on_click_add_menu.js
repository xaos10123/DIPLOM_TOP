items = document.querySelectorAll('.item');
items_open = [];



items.forEach((element) => {
    element.addEventListener('click', (evt) => {
        evt.stopPropagation();
        closeAllMenuAddToBasket();
        const item = evt.currentTarget;
        const id = item.getAttribute('data-item-id');
        const name = item.querySelector('.item_name').textContent;
        const characteristic = item.querySelector('.item_characteristic').textContent;

        const baseContainer = item.querySelector('.base_container_item');

        if (!baseContainer.getAttribute('data-has-menu')) {
            baseContainer.innerHTML += createTemplate(id, name, characteristic);
            baseContainer.setAttribute('data-has-menu', true);
        }

        const menu = baseContainer.querySelector('.item_add_to_card');

        disp = getComputedStyle(menu).display;
        if (disp == 'none') {
            menu.style.display = 'block';
            items_open.push(item);
        } else {
            menu.style.display = 'none';
            itemIndex = items_open.indexOf(item);
            items_open.splice(itemIndex, 1);
        }
    });
});

document.addEventListener('click', () => {
    if (items_open.length == 0) {
        return
    }
    closeAllMenuAddToBasket();
});

document.onscroll = () => {
    if (items_open.length == 0) {
        return
    }
    closeAllMenuAddToBasket();
}

function closeAllMenuAddToBasket() {
    console.log('closeAllMenuAddToBasket');
    
    items_open.forEach((item, index) => {
        const menu = item.querySelector('.item_add_to_card');
        menu.style.display = 'none';
        items_open.splice(index, 1);
    });
}


function chenge_value(evt, to) {
    evt.stopPropagation();

    const btn = evt.currentTarget;

    to == 'up' ? valuesElement = btn.previousElementSibling : valuesElement = btn.nextElementSibling;

    var value_number = parseInt(valuesElement.textContent);

    if (to == 'up') {
        value_number++;
    } else {
        if (value_number == 1) {
            return
        }
        value_number--;
    }

    valuesElement.textContent = value_number;
    btn.parentNode.parentNode.parentNode.setAttribute('data-count', value_number);
}



function addToBasketFromMenu(evt, id) {
    const countElement = evt.currentTarget.parentNode.parentNode.parentNode;
    count = parseInt(countElement.getAttribute('data-count'));
    countElement.setAttribute('data-count', 1);
    countElement.querySelector('.item_value').textContent = 1;

    console.log({ "id": id, "count": count });

    return { "id": id, "count": count };
}

function createTemplate(id, name, characteristic) {
    return `
        <div class="item_add_to_card" data-count="1">
                    <div
                      class="container d-flex flex-column align-items-center justify-content-center text-center h-100">
                      <div class="item_name fs-5">${name}</div>
                      <div class="item_characteristic fs_n_thin_italic text-white">${characteristic}
                      </div>
                      <div class="row">
                        <div class="col fs_n_thin_italic fs-6 pt-4">Количество:</div>
                      </div>
                      <div class="row text-black pt-3 w-75">
                        <button class="btn btn-light col-3 fs-6 p-0" type="button" onclick="chenge_value(event, 'down')"><i
                            class="fa-solid fa-chevron-down"></i></button>
                        <div class="col-6 text-center text-white p-0 px-3 fs-5 item_value">1</div>
                        <button class="btn btn-light col-3 fs-6 p-0" type="button" onclick="chenge_value(event, 'up')"><i
                            class="fa-solid fa-chevron-up"></i></button>
                      </div>
                      <div class="row w-100 pt-3">
                        <button class="btn btn-primary col fs-6 py-2" type="button" onclick="addToBasketFromMenu(event, ${id})">В корзину</button>
                      </div>
                    </div>
                  </div>
        `;
}
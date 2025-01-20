function showNotification(message, type = 'success') {

    const notification = document.createElement('div');
    notification.className = `alert alert-${type} notification-toast`;
    notification.style.cssText = `
        position: fixed;
        top: 30px;
        right: calc(50% - 200px);
        z-index: 1000;
        width: 400px;
        padding: 15px;
        border-radius: 20px;
        animation: slideIn 0.5s ease-in-out;
        font-family: "NerisThin", sans-serif;
    `;
    
    notification.innerHTML = message;


    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideIn {
            from { transform: translateY(100%); }
            to { transform: translateY(0); }
        }
        @keyframes fadeOut {
            from { opacity: 1; }
            to { opacity: 0; }
        }
    `;
    document.head.appendChild(style);


    document.body.appendChild(notification);

 
    setTimeout(() => {
        notification.style.animation = 'fadeOut 0.5s ease-in-out';
        setTimeout(() => {
            notification.remove();
        }, 500);
    }, 3000);
}




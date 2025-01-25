function showNotification(message, type = 'success') {

    const notification = document.createElement('div');
    notification.className = `alert alert-${type} notification-toast shadow`;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 50%;
        z-index: 10000;
        width: 100%;
        max-width: 400px;
        padding: 15px;
        border-radius: 20px;
        transform: translateX(50%);
        animation: slideIn 0.5s ease-in-out;
        font-family: "NerisThin", sans-serif;
    `;
    
    notification.innerHTML = message;


    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideIn {
            from { transform: translateY(100%) translateX(50%); }
            to { transform: translateY(0) translateX(50%); }
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




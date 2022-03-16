// import css from './notice.css'

!function () {
    "use strict"

    class Notice {
        showLoading(options) {
            typeof options !== 'object' || options === null ? options = {} : '';

            // set Default Value
            const type = options.type || 'line',
                color = options.color || '#ffffff',
                backgroundColor = options.backgroundColor || 'rgba(0,0,0,.6)',
                title = options.title || '',
                fontSize = !!(Number(options.fontSize)) ? Number(options.fontSize) : 16;

            // create Parent Element
            const container = document.createElement('div');
            container.setAttribute('class', 'notice-loading notice-flex-center notice-fixed-all-page');
            container.setAttribute('id', 'notice-loading');

            // get Loading Element
            const loadingEl = getLoadingEl(type, color);


            container.innerHTML = `
                <div class="notice-mask notice-fixed-all-page" style="background-color: ${backgroundColor}"></div>
                <div class="notice-flex-center notice-loading-main">
                ${loadingEl}
                    ${title ? `<p style="color:${color};font-size: ${fontSize + 'px'};">${title}</p>` : ''}
                </div>
            `;
            $('body').appendChild(container);
        }

        hideLoading() {
            const loadingEl = $('#notice-loading');
            if (loadingEl) {
                $('body').removeChild(loadingEl)
            }
        }

        showToast(options) {
            typeof options !== 'object' || options === null ? options = {} : '';

            const text = options.text;
            // if not text , cannot show toast
            if(!text) return ;

            // get screen width
            const isPhone = screen.width < 576;

            // set Default Value
            const typeStyles = {
                default: {icon: '', phoneIcon: '', color: '#909399', backgroundColor: '#f4f4f5'},
                success: {icon: '&#xe66b;', phoneIcon: '&#xe600;', color: '#67c23a', backgroundColor: '#f0f9eb'},
                error: {icon: '&#xe651;', phoneIcon: '&#xe640;', color: '#e6a23c', backgroundColor: '#fdf6ec'},
                info: {icon: '&#xe89e;', phoneIcon: '&#xea11;', color: '#909399', backgroundColor: '#f4f4f5'},
                warning: {icon: '&#xe65b;', phoneIcon: '&#xea0c;', color: '#f56c6c', backgroundColor: '#fef0f0'},
            }
            const type = options.type || 'default';
            const typeStyle = typeStyles[type] || typeStyles['default'];
            isPhone ? typeStyle.icon = typeStyle.phoneIcon : '';

            let autoClose = typeof options.autoClose === "boolean" ? options.autoClose : true;
            typeStyle.showClose = options.showClose || false;
            typeStyle.text = text;


            const toastElementId = getElId('notice-toast');

            // if isPhone
            if(isPhone) {
                typeStyle.icon = typeStyle.phoneIcon;
                autoClose = true;

                if($('#notice-toast')){
                    $('#notice-toast').remove();
                }
            }

            // Determine if toast exists
            if ($('#notice-toast')) {
                // create Element
                const main = document.createElement('div');
                main.setAttribute('class', 'notice-toast-main');
                main.setAttribute('id', toastElementId);
                main.setAttribute('style', `background:${typeStyle.backgroundColor}`);
                main.innerHTML = getToastEl(toastElementId,typeStyle,isPhone);
                $('#notice-toast').appendChild(main);
            } else {
                // create Parent Element
                const container = document.createElement('div');
                container.setAttribute('class', 'notice-toast');
                container.setAttribute('id', 'notice-toast');
                container.innerHTML =
                    ` <div class="notice-toast-main" id="${toastElementId}" 
                        style="background:${typeStyle.backgroundColor}">
                    ${getToastEl(toastElementId,typeStyle,isPhone)}
                </div> `;
                $('body').appendChild(container);
            }

            // show animation
            setTimeout(() => $(`#${toastElementId}`).classList.add('notice-toast-main-active'));

            // Turn off regularly
            if(autoClose){
                setTimeout(() => {
                    const el = $(`#${toastElementId}`);
                    if(el){
                        el.classList.remove('notice-toast-main-active');
                        setTimeout(() => el.remove(), 500);
                    }
                }, 4000);
            }
        }
    }

    function $(el, con) {
        return typeof el === 'string' ? (con || document).querySelector(el) : el || null;
    }

    function getLoadingEl(type, color) {
        switch (type) {
            case 'cube_flip':
                return `<div class="notice-loading-cube-flip" style="background-color: ${color}"></div>`;
                break;
            case 'dots_zoom':
                return `<div class="notice-loading-dots-zoom">
                        <div class="notice-loading-dots-zoom1" style="background-color: ${color}"></div>
                        <div class="notice-loading-dots-zoom2" style="background-color: ${color}"></div>
                    </div>`;
                break;
            case 'line' :
                return `<div class="notice-loading-line">
                      <div class="notice-loading-line-rect1" style="background-color: ${color}"></div>
                      <div class="notice-loading-line-rect2" style="background-color: ${color}"></div>
                      <div class="notice-loading-line-rect3" style="background-color: ${color}"></div>
                      <div class="notice-loading-line-rect4" style="background-color: ${color}"></div>
                      <div class="notice-loading-line-rect5" style="background-color: ${color}"></div>
                    </div>`
                break;
            case 'dots_spin':
                return `<div class="notice-loading-spin-dots">
                      <div class="notice-loading-spin-dot1" style="background-color: ${color}"></div>
                      <div class="notice-loading-spin-dot2" style="background-color: ${color}"></div>
                    </div>`
                break;
            case 'dots' :
                return `<div class="notice-loading-dots">
                      <div class="notice-loading-dot1" style="background-color: ${color}"></div>
                      <div class="notice-loading-dot2" style="background-color: ${color}"></div>
                      <div style="background-color: ${color}"></div>
                    </div>`
                break;
            case 'cube_zoom' :
                return `<div class="notice-loading-cube-zoom">
                      <div class="notice-loading-cube-zoom-1" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-2" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-3" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-4" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-5" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-6" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-7" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-8" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-9" style="background-color: ${color}"></div>
                    </div>`
                break;
        }
    }

    function getToastEl(id, {color,icon,showClose,text},isPhone) {
        return ` <div class="notice-toast-container">
                    ${icon ? `<i class="notice-iconfont notice-toast-icon" style="color: ${color}">${icon}</i>` : ''}
                    <p class="notice-toast-text ${isPhone && !icon  ? 'notice-toast-truncate-second' : ''}" style="color: ${color}; max-width: ${showClose ? 'calc(80vw - 125px)' : 'calc(80vw - 95px)'};">${text}</p> 
                </div>
                ${  showClose ?
                    `<i class="notice-iconfont notice-close-icon"
                       onclick="
                            document.getElementById('${id}').classList.remove('notice-toast-main-active');
                            setTimeout(() => document.getElementById('${id}').remove(), 500);">
                        &#xe73e;
                    </i>`  : ''
                }`
    }

    // get only id
    function getElId(text) {
        return text + '-' + Number(Math.random().toString().substr(3, 4) + Date.now()).toString(36);
    }

    window.Notice = Notice;
}()
server {
    listen 80;
    server_name tommorow-techs.com www.tommorow-techs.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name tommorow-techs.com www.tommorow-techs.com;

    ssl_certificate /etc/letsencrypt/live/tommorow-techs.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/tommorow-techs.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    root /home/bezbak/tt_build;
    index index.html;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        try_files $uri $uri/ /index.html;
    }

    location /assets/ {
        alias /home/bezbak/tt_build/assets/;
        access_log off;
        expires 30d;
    }

    location ~* \.(?:ico|css|js|gif|jpe?g|png|svg|woff2?|ttf|otf|eot)$ {
        root /home/bezbak/tt_build;
        access_log off;
        expires 30d;
    }
}

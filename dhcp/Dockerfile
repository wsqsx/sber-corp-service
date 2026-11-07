FROM alpine:3.20
RUN apk add --no-cache dhcp bind-tools
COPY dhcpd.conf /etc/dhcp/dhcpd.conf
CMD ["dhcpd", "-f", "-d", "-cf", "/etc/dhcp/dhcpd.conf"]
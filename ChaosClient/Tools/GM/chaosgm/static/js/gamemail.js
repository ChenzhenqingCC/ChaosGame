/**
 * Created by wallace&lily on 2016/2/27.
 */

var MailForm = {
    create: function () {
        var form = {};

        form.validate = function () {
            this.errors = [];
            this.need_check = [];

            if (this.server_num == 0) {
                this.errors.push(gettext("please_choose_server"))
            }

            if (!this.is_whole_accounts) {
                if (this.server_num > 1) {
                    this.errors.push(gettext("nowhole_server_mail_can_only_select_one_server"))
                }
                if (this.accounts_str.length == 0) {
                    this.errors.push(gettext("nowhole_server_mail_must_has_target_account"))
                }
                this.need_check.push({'type': "accounts", value: this.accounts})
            }

            if ($("form #id_send_date_0").val().length == 0 || $("form #id_send_date_1").val().length == 0) {
                this.errors.push(gettext("no_send_date"))
            }

            var items = this.items;
            for (var i = 0; i < items.length; i++) {
                var item = items[i];
                if (item.item_type == "item") {
                    if (!IsNum(item.item_id)) {
                        this.errors.push(gettext("item_must_have_id"))
                    }
                    this.need_check.push({'type': "item", value: item})
                }
                if (!IsNum(item.num)) {
                    this.errors.push(gettext("attach_num_must_be_number"))
                }
            }
        };

        form.update = function () {
            this.server_num = $("form #id_server_list_to option").length;
            this.is_whole_accounts = $("form #id_whole_accounts").is(':checked');
            var accounts_str = $.trim($("form #id_accounts").val());
            this.accounts_str = accounts_str;

            var servers = [];
            this.servers = servers;
            $("form #id_server_list_to option").each(
                function (index, option) {
                    var option_j = $(option);
                    servers.push({id: option_j.val(), name: option_j.text()});
                });

            this.accounts = [];
            var a_strs = accounts_str.split(",");
            for (var ai = 0; ai < a_strs.length; ai++) {
                var account_id = a_strs[ai];
                this.accounts.push({id: account_id})
            }

            this.items = [];
            var items = $("tr[data-choose]");
            for (var i = 0; i < items.length; i++) {
                var item = items[i];
                var tds = item.childNodes;
                var item_type = $(item).attr("data-choose");
                var id = $(tds[1]).find("input").val();
                var num = $(tds[2]).find("input").val();
                this.items.push({'item_id': id, 'item_type': item_type, 'num': num})
            }
            this.validate();
        };

        form.get_item_by_id = function (id) {
            for (var i = 0; i < this.items.length; i++) {
                var item = this.items[i];
                if (item.item_id == id.toString()) {
                    return item
                }
            }
        };

        form.get_account_by_id = function (id) {
            for (var i = 0; i < this.accounts.length; i++) {
                var account = this.accounts[i];
                if (account.id == id.toString()) {
                    return account
                }
            }
        };

        return form
    }
};

(function ($) {
    $(function () {
        var rows = 1;
        var mail_form = MailForm.create();
        $("form #item_table").css("visibility", "hidden");
        $('#id_add_btns a').click(function (e) {
            var data_type = $(this).attr("data-type");
            var content = "<tr data-choose='" + data_type + "'><td>" + $(this).text() + "</td>"
            if (data_type == 'item') {
                content = content + "<td><input placeholder=\'" + gettext("please_enter_id") + "\'/></td>"
            }
            else {
                content = content + "<td></td>"
            }
            content = content + "<td><input placeholder=\'" + gettext("please_enter_num") + "\'/></td><td><a herf='#' id='del_link_" + rows + "' class: 'fui-cross' onmouseover='' style='cursor: pointer;' >x</a></td></tr>"
            $("#id_item_tbl_body").append(content);

            $("form #item_table").css("visibility", "visible");

            $('#del_link_' + rows).click(function (e) {
                var row = $(this).parent().parent();
                var data_type = row.attr("data-choose");
                row.remove();

                rows = rows - 1
            });
            e.preventDefault();
            rows = rows + 1;
            return false;
        });

        function show_erros(error_list) {
            var content = "<ul>";
            for (var i = 0; i < error_list.length; i++) {
                content = content + "<li>" + error_list[i] + "</li>"
            }
            content = content + "</ul>";
            $('.modal').find('#id_error_body_content').empty().append(content);
            $('#errorModel').modal()
        }

        $('#gamemail_form').on('submit', function (e) {
            if (e.isDefaultPrevented()) {

            } else {
                event.preventDefault();
                mail_form.update();
                var errors = mail_form.errors;
                if (errors.length == 0) {
                    var need_check = mail_form.need_check;
                    if (need_check.length == 0) {
                        $('#confirmModel').modal()
                    }
                    else {
                        var json_str = JSON.stringify(need_check);
                        var servers_str = JSON.stringify(mail_form.servers);
                        waitingDialog.show(gettext("validating"), {dialogSize: 'sm', progressType: 'warning'});
                        $.ajax({
                            url: "/gamemail_validate",
                            type: "POST",
                            data: {need_check: json_str, csrfmiddlewaretoken: csrf_token,servers:servers_str},
                            dataType: 'json',
                            success: function (rsp_obj) {
                                waitingDialog.hide();
                                var error_list = rsp_obj.error_list;
                                if (error_list && error_list.length > 0) {
                                    error_descs = [];
                                    for (var e_i = 0; e_i < error_list.length; e_i++) {
                                        var error = error_list[e_i];
                                        if (error.type == 'item_not_exist') {
                                            error_descs.push(gettext("item_not_exist") + ":" + error.value.item_id)
                                        }
                                        else if (error.type == 'account_not_exist') {
                                            error_descs.push(gettext("account_not_exist") + ":" + error.value.id)
                                        }
                                    }
                                    show_erros(error_descs)
                                }
                                else {
                                    var info_list = rsp_obj.info_list;
                                    for (var i = 0; i < info_list.length; i++) {
                                        var iter_info = info_list[i];
                                        if (iter_info.type == "item") {
                                            var item_in_form = mail_form.get_item_by_id(iter_info.value.id);
                                            if (item_in_form) {
                                                item_in_form.name = iter_info.value.name
                                            }
                                        }
                                        else if (iter_info.type == "account") {
                                            var account_in_form = mail_form.get_account_by_id(iter_info.value.id);
                                            if (account_in_form) {
                                                account_in_form.name = iter_info.value.name
                                            }
                                        }
                                    }

                                    $('#confirmModel').modal()
                                }
                            },
                            error: function (rsp_obj) {
                                waitingDialog.hide();
                                var fail_str = gettext("validate_fail");
                                $.toaster({priority: 'danger', title: fail_str, message: rsp_obj.status});
                            }
                        });
                    }
                }
                else {
                    show_erros(errors);
                }
            }
        });


        var check_box = $('form #id_whole_accounts');
        if (check_box.is(':checked')) {
            $('form #id_account_collapse').collapse('hide')
        }

        check_box.change(function () {
            $('form #id_account_collapse').collapse('toggle')
        });


        var temp = '<ul>'+
                            '<li>'+ gettext("target_server") +
                                '<ul>'+
                                   '{0}'+
                                '</ul>'+
                            '</li>'+
                            '<li>'+ gettext("target_account") +
                                '<ul>'+
                                   '{1}'+
                                '</ul>'+
                            '</li>'+
                            '<li>' + gettext("send_date") + ':{2}</li>'+
                            '<li>'+gettext("attachment")+
                                '<ul>'+
                                   '{3}'+
                                '</ul>'+
                            '</li>'+
                        '</ul>';

        var item_li_temp = '<li>{0}</li>';


        $('#confirmModel').on('show.bs.modal', function (event) {
            var modal = $(this);

            var items = mail_form.items;

            var item_str = "";
            var json_obj = [];
            for (var i = 0; i < items.length; i++) {
                var item = items[i];

                json_obj.push({"item_type": item.item_type, "item_id": item.item_id, "num": item.num});

                var id = item.item_id;
                if (id == undefined) {
                    id = ""
                }

                var item_line_str = item.item_type + " " + id + " " + gettext("num") + ": " + item.num;
                if (item.name) {
                    item_line_str = item_line_str + " " + gettext("item_name") + ": " + item.name
                }

                var line = item_li_temp.format(item_line_str);
                item_str = item_str + line
            }

            var server_str = "";

            $("form #id_server_list_to option").each(
                function (index, option) {
                    server_str = server_str + item_li_temp.format($(option).text())
                });

            var accounts_str = "";
            if (mail_form.is_whole_accounts) {
                accounts_str = item_li_temp.format(gettext("whole_server"))
            }
            else {
                var accounts = mail_form.accounts;
                for (var ai = 0; ai < accounts.length; ai++) {
                    var account = accounts[ai];
                    accounts_str = accounts_str + item_li_temp.format("ID: " + account.id + " " + gettext("account_name") + ": " + account.name)
                }
            }
            var time = $("form #id_send_date_0").val() + " " + $("form #id_send_date_1").val();

            if (item_str == "") {
                item_str = gettext("none")
            }
            var out = temp.format(server_str, accounts_str, time, item_str);
            modal.find('#id_model_body_content').empty().append(out);

            modal.find(".btn-primary").click(function (e) {
                $('#id_hidden_items').val(JSON.stringify(json_obj));
                SelectBox.select_all('id_server_list_to');
                $('#gamemail_form').submit()
            });

        })
    });


})(jQuery);
import React, { Component } from 'react';
import { Layout, Menu } from 'antd';
const { Header, Content, Footer } = Layout;

class HeaderContentFooter extends Component {
  render() {
    return (
      <Layout>
        <Header>
            <Menu
                mode="horizontal"
                theme="dark"
                style={{lineHeight: '64px'}}
            >
                <Menu.Item key="1">MyAppName</Menu.Item>
                <Menu.Item key="2">nav 1</Menu.Item>
                <Menu.Item key="3">nav 2</Menu.Item>
                <Menu.Item key="4">nav 3</Menu.Item>
            </Menu>
        </Header>
        <Content style={{
            padding: '5em',
        }}>
        some kind of content
        </Content>
        <Footer>

        </Footer>
      </Layout>
    );
  }
}

export default HeaderContentFooter;

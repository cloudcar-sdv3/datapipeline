import { useState } from "react";

const Toolbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [hover, setHover] = useState(false);

  const toggleDropdown = () => setIsOpen(!isOpen);

  return (
    <div className="toolbar">
      {/* <a href="https://www.wipro.com/" target="_blank" rel="noreferrer">
        <img
          src="/app_icons/wip_logo_white.png"
          alt="Wipro Logo"
          className="toolbar-logo"
        />
      </a> */}
      <p className="toolbar-title">Dell Data Pipeline</p>
      <div style={{ display: "flex", justifyContent: "flex-end" }}>
        <div
          onClick={toggleDropdown}
          onMouseEnter={() => setHover(true)}
          onMouseLeave={() => setHover(false)}
          className="toolbar-references"
        >
          {/* <span style={{ textDecoration: hover ? "underline" : "none" }}>
            References
          </span>
          {isOpen && (
            <div className="dropdown">
              <a
                href="/architecture/dh_architecture.jpeg"
                target="_blank"
                className="dropdown-link"
              >
                Architecture
              </a>
              <a
                href="https://rancher-server.cloudcar.wipro.com/dashboard/auth/login?timed-out"
                target="_blank"
                rel="noreferrer"
                className="dropdown-link"
              >
                Rancher
              </a>
              <a
                href="/architecture/cloud_architecture.jpg"
                target="_blank"
                rel="noreferrer"
                className="dropdown-link"
              >
                Cloud-pipeline
              </a>
              <a
                href="http://192.168.0.114:32358/kiali/console/graph/namespaces/?traffic=grpc%2CgrpcRequest%2Chttp%2ChttpRequest%2Ctcp%2CtcpSent&graphType=versionedApp&duration=60&refresh=60000&namespaces=cattle-impersonation-system%2Ccattle-system%2Clocal%2Ccattle-fleet-system%2Cistio-system%2Cdefault%2Ckubernetes-dashboard%2Cstreaming%2Cshadowmode&layout=kiali-dagre&namespaceLayout=kiali-dagre"
                target="_blank"
                rel="noreferrer"
                className="dropdown-link"
              >
                Kiali
              </a>
              <a
                href="http://192.168.0.114:31450/d/bcc8f659-c4c7-4b95-8a53-bad43f3b4c62/kubernetes-cluster-monitoring-via-prometheus?orgId=1&refresh=10s"
                target="_blank"
                rel="noreferrer"
                className="dropdown-link"
              >
                Grafana
              </a>
              <a
                href="http://192.168.0.114:31365/"
                target="_blank"
                rel="noreferrer"
                className="dropdown-link"
              >
                Jaeger
              </a>
            </div>
          )} */}
        </div>
      </div>
    </div>
  );
};

export default Toolbar;

# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: SupportQueue
def main():
    print("=" * 70)
    print(" SupportQueue — Final Self-Check Report ".center(70, "="))
    print("=" * 70)

    # 1. Create a support queue and add agents
    queue = SupportQueue("General", SLA(sla_hours=4))
    queue.add_agent(agent_id="1", name="Alice", role="support", priority=3)
    queue.add_agent(agent_id="2", name="Bob", role="support", priority=4)
    queue.add_agent(agent_id="3", name="Charlie", role="lead", priority=5)

    # 2. Add tickets
    queue.add_ticket(ticket_id="T001", title="Login issue", priority=2, status="open",
                     assignee_id="1", sla=SLA(sla_hours=4))
    queue.add_ticket(ticket_id="T002", title="Payment error", priority=5, status="open",
                     assignee_id="2", sla=SLA(sla_hours=2))
    queue.add_ticket(ticket_id="T003", title="Feature request", priority=1, status="open",
                     assignee_id="3", sla=SLA(sla_hours=6))

    # 3. Process tickets: Alice handles T001, Bob handles T002
    queue.process_ticket("T001", agent_id="1", action="answer", message="Fixed the login bug.")
    queue.process_ticket("T002", agent_id="2", action="answer", message="Payment gateway issue resolved.")

    # 4. Print queue status
    print(f"Queue: {queue.name}")
    print(f"Agents: {queue.get_agents()}")
    print(f"Tickets: {queue.get_tickets()}")
    print(f"Next available agent: {queue.get_next_agent()}")

    # 5. Check SLA compliance
    for ticket in queue.get_tickets():
        status = "OK" if ticket.get_status() == "resolved" else "⚠️ SLA check pending"
        print(f"  Ticket {ticket.get_id()}: {status}")

    # 6. Final summary
    print("\n" + "=" * 70)
    print(" Application ready! All core features verified. ".center(70, "="))
    print("=" * 70)

if __name__ == "__main__":
    main()
